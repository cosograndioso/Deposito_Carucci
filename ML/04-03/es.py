from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import math
import os
import xgboost as xgb
import optuna
from sklearn.metrics import f1_score

# Scarica il dataset Spaceship Titanic tramite il suo ID o nome su OpenML
# L'ID 44096 è comunemente associato alla versione "Spaceship Titanic"

# Costruisce il percorso assoluto del file 'train.csv' partendo dalla posizione dello script.
# In questo modo, lo script troverà sempre il file, indipendentemente da dove viene eseguito.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'train.csv')

# Carica il dataset dal file locale nella stessa cartella dello script
try:
    df = pd.read_csv(file_path)
    print("Dataset caricato con successo!")
    print("-" * 30)
    print(df.head())
    print("-" * 30)
    print(df.info())
except FileNotFoundError:
    print(f"ERRORE: File non trovato al percorso '{file_path}'.")
    print("Assicurati di aver incollato il file 'train.csv' nella cartella '04-03'!")

for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category')

df[['Cabin_Deck', 'Cabin_Num', 'Cabin_Side']] = df['Cabin'].str.split('/', expand=True)

# Ora che abbiamo estratto le info, possiamo eliminare la colonna originale 'Cabin'
df = df.drop('Cabin', axis=1)
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

categorical_cols = df.select_dtypes(include=['category', 'object']).columns
for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])



print("\n--- NUOVO RAPPORTO DANNI ---")
print(df.isnull().sum())
print("-" * 30)
print("Riparazione completata! Dati pronti per l'addestramento.")

# --- VISUALIZZAZIONE DATI ---
# Impostiamo lo stile di Seaborn
sns.set_theme(style="whitegrid")

# 1. Grafico a torta per la variabile target 'Transported'
plt.figure(figsize=(6, 6))
df['Transported'].value_counts().plot.pie(autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
plt.title('Percentuale Passeggeri Trasportati')
plt.ylabel('')
plt.show()

# 2. Istogramma dell'Età diviso per 'Transported'
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Transported', kde=True, bins=30, palette='coolwarm')
plt.title('Distribuzione Età: Trasportati vs Non Trasportati')
plt.show()

# 3. Conteggio per Pianeta di Origine e Destinazione
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.countplot(data=df, x='HomePlanet', hue='Transported', palette='viridis', ax=axes[0])
axes[0].set_title('Trasportati per Pianeta di Origine')

sns.countplot(data=df, x='Destination', hue='Transported', palette='magma', ax=axes[1])
axes[1].set_title('Trasportati per Destinazione')

plt.tight_layout()
plt.show()

# 4. Matrice di Correlazione
plt.figure(figsize=(10, 8))
# Convertiamo Transported in numero per vederlo nella matrice
df_corr = df.copy()
df_corr['Transported'] = df_corr['Transported'].astype(int)
# Selezioniamo solo le colonne numeriche
numeric_df = df_corr.select_dtypes(include=['number'])
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matrice di Correlazione')
plt.show()

print("\nPreparazione dei dati per il Machine Learning...")

# 1. Eliminiamo identificatori inutili
df = df.drop(['PassengerId', 'Name'], axis=1)

# 2. Convertiamo Cabin_Num in numero (era rimasto testo dopo lo split)
df['Cabin_Num'] = pd.to_numeric(df['Cabin_Num'])

# 3. Convertiamo i booleani (True/False) in 1 e 0
booleane = ['CryoSleep', 'VIP', 'Transported']
for col in booleane:
    df[col] = df[col].astype(int)


df = pd.get_dummies(df, columns=['HomePlanet', 'Destination', 'Cabin_Deck', 'Cabin_Side'], drop_first=True)


X = df.drop('Transported', axis=1)
y = df['Transported']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

ratio = len(y_train[y_train==0]) / len(y_train[y_train==1])

def objective(trial):
    param = {
        'verbosity': 0,
        'objective': 'binary:logistic',
        'eval_metric': 'logloss',
        'tree_method': 'hist', 
        'n_jobs' : -1,
        
        # Hyperparameters
        'scale_pos_weight': trial.suggest_float('scale_pos_weight', ratio * 0.8, ratio * 1.2),
        'lambda': trial.suggest_float('lambda', 1e-8, 1.0, log=True),
        'alpha': trial.suggest_float('alpha', 1e-8, 1.0, log=True),
        'subsample': trial.suggest_float('subsample', 0.5, 1.0),
        'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
        'max_depth': trial.suggest_int('max_depth', 3, 10),
        'learning_rate': trial.suggest_float('learning_rate', 0.01, 0.2, log=True),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        
    }
    
    
    
    pruning_callback = optuna.integration.XGBoostPruningCallback(trial, 'eval-logloss')

    # 2. Addestramento del modello XGBoost per questo specifico tentativo
    bst = xgb.train(
        param, 
        dtrain, 
        num_boost_round=400, # Numero massimo di iterazioni/alberi
        evals=[(dtest, 'eval')],
        callbacks=[pruning_callback],
        verbose_eval=False # Nasconde i log noiosi di ogni singolo albero
    )

    # 3. Previsioni sulle probabilità e conversione binaria (0 o 1)
    preds_prob = bst.predict(dtest)
    preds = [1 if p > 0.5 else 0 for p in preds_prob]

    # 4. Ritorna l'F1-score (il voto che Optuna cercherà di massimizzare)
    return f1_score(y_test, preds)

# ==========================================
# FASE 5: AVVIO DELLO STUDY DI OPTUNA
# ==========================================
print("\n🚀 Avvio dell'ottimizzazione degli iperparametri con Optuna...")

# Impostiamo i log per vedere cosa sta facendo
optuna.logging.set_verbosity(optuna.logging.INFO)

# Creiamo lo "Study"
study = optuna.create_study(
direction='maximize', 
pruner=optuna.pruners.MedianPruner(n_warmup_steps=5)
)

# Avviamo il torneo! Facciamo 20 tentativi per ora (puoi alzarlo a 50 o 100 in futuro)
study.optimize(objective, n_trials=20, show_progress_bar=True)

# ==========================================
# FASE 6: RISULTATI FINALI
# ==========================================
print("\n" + "="*40)
print("🏆 OTTIMIZZAZIONE COMPLETATA! 🏆")
print("="*40)
print(f"Miglior  ottenuto: {study.best_trial.value:.4f}")
print("\nMigliori Parametri trovati:")
for key, value in study.best_params.items():
 print(f"  '{key}': {value},")
    
    
print("\n" + "="*40)
print("🚀 ADDESTRAMENTO DEL MODELLO DEFINITIVO")
print("="*40)

# 1. Recuperiamo i parametri statici di base
best_params = {
    'verbosity': 0,
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'tree_method': 'hist', 
    'n_jobs' : -1
}

# 2. Aggiungiamo i parametri vincenti trovati da Optuna
best_params.update(study.best_params)

# 3. Addestriamo il modello "Super-XGBoost" (questa volta senza il pruner, lo facciamo girare fino in fondo)
final_model = xgb.train(
    best_params, 
    dtrain, 
    num_boost_round=300, 
    evals=[(dtest, 'eval')],
    verbose_eval=50 # Ci stampa un aggiornamento ogni 50 alberi creati
)

# 4. Calcoliamo l'accuratezza finale per sicurezza
final_preds_prob = final_model.predict(dtest)
final_preds = [1 if p > 0.5 else 0 for p in final_preds_prob]

from sklearn.metrics import accuracy_score, classification_report
print("\n--- RISULTATI SUL SET DI TEST ---")
print(f"F1-Score Finale: {f1_score(y_test, final_preds):.4f}")
print(f"Accuratezza Finale: {accuracy_score(y_test, final_preds):.4f}")
print("\nReport Completo:")
print(classification_report(y_test, final_preds))




print("\n" + "="*40)
print("🛸 ANALISI DEI PASSEGGERI DISPERSI (test.csv)")
print("="*40)

# 1. Carichiamo i veri passeggeri da prevedere
test_path = os.path.join(script_dir, 'train.csv')
try:
    df_test = pd.read_csv(test_path)
    print("File 'test.csv' caricato con successo! Inizio analisi...")
except FileNotFoundError:
    print(f"ERRORE: File 'test.csv' non trovato. Scaricalo da Kaggle e mettilo nella cartella.")
    exit()

# Salviamo l'ID dei passeggeri da parte, ci servirà alla fine per il file dei risultati
passenger_ids = df_test['PassengerId']

# 2. APPLICHIAMO LE STESSE IDENTICHE TRASFORMAZIONI DEL TRAIN SET
# Splittiamo la cabina
df_test[['Cabin_Deck', 'Cabin_Num', 'Cabin_Side']] = df_test['Cabin'].str.split('/', expand=True)

# Eliminiamo le colonne inutili
df_test = df_test.drop(['Cabin', 'PassengerId', 'Name'], axis=1)

# Convertiamo in numero
df_test['Cabin_Num'] = pd.to_numeric(df_test['Cabin_Num'])

# Ripariamo i buchi usando le mediane e mode che abbiamo trovato prima
for col in numeric_cols:
    if col in df_test.columns:
        df_test[col] = df_test[col].fillna(df_test[col].median())

for col in categorical_cols:
    if col in df_test.columns:
        df_test[col] = df_test[col].fillna(df_test[col].mode()[0])

# Booleani in numeri (Attenzione: qui NON c'è la colonna 'Transported'!)
booleane_test = ['CryoSleep', 'VIP']
for col in booleane_test:
    df_test[col] = df_test[col].astype(int)

# One-Hot Encoding
df_test = pd.get_dummies(df_test, columns=['HomePlanet', 'Destination', 'Cabin_Deck', 'Cabin_Side'], drop_first=True)

# 3. ALLINEAMENTO DELLE COLONNE (Passaggio Cruciale!)
# È possibile che nel test set manchino alcune categorie presenti nel train set.
# Dobbiamo assicurarci che df_test abbia esattamente le stesse colonne di X (il nostro train set originale)
df_test = df_test.reindex(columns=X.columns, fill_value=0)

# 4. IL MOMENTO DELLA VERITÀ: PREVISIONI!
# Creiamo la matrice per XGBoost
dtest_final = xgb.DMatrix(df_test)

# Chiediamo al modello di prevedere la probabilità
previsioni_prob = final_model.predict(dtest_final)

# Kaggle vuole le risposte nel formato True/False, quindi riconvertiamo:
# Se la probabilità è > 50%, diciamo True (Trasportato), altrimenti False.
previsioni_finali = [True if p > 0.5 else False for p in previsioni_prob]

# 5. CREAZIONE DEL FILE DI SALVATAGGIO PER KAGGLE
submission = pd.DataFrame({
    'PassengerId': passenger_ids,
    'Transported': previsioni_finali
})

# Filtra solo i passeggeri che sono stati trasportati (True)
submission = submission[submission['Transported'] == True]

# Salviamo il file in CSV (index=False evita che Pandas aggiunga una colonna inutile coi numeri di riga)
submission_path = os.path.join(script_dir, 'submission.csv')
submission.to_csv(submission_path, index=False)

print(f"\n✅ MISSIONE COMPIUTA! Previsioni salvate in: {submission_path}")
print("Ora puoi caricare il file 'submission.csv' su Kaggle per vedere il tuo punteggio!")