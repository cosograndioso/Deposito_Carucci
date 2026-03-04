import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

# 1. Caricamento e Preparazione dei Dati
# Usiamo il dataset Titanic integrato in Seaborn
df = sns.load_dataset('titanic')

# Selezione delle feature più importanti
# pclass: classe biglietto, sibsp: fratelli/coniugi, parch: genitori/figli, fare: tariffa
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'family_size', 'is_alone', 'who', 'deck', 'fare_per_person']
target = 'survived'

# --- Pulizia Dati ---
# Riempiamo i valori mancanti (NaN)
# Miglioramento: Riempiamo l'età usando la mediana specifica per Classe e Sesso (più preciso)
df['age'] = df['age'].fillna(df.groupby(['pclass', 'sex'])['age'].transform('median'))
df['embarked'] = df['embarked'].fillna(df['embarked'].mode()[0])  # Porto imbarco con la moda

# Feature Engineering: Creiamo nuove variabili
df['family_size'] = df['sibsp'] + df['parch'] + 1  # +1 include il passeggero stesso
df['is_alone'] = 0
df.loc[df['family_size'] == 1, 'is_alone'] = 1  # 1 se viaggia da solo
df['fare_per_person'] = df['fare'] / df['family_size'] # Costo reale per persona

# Gestione colonna 'deck' (ponte) e 'who' (uomo/donna/bambino)
# Il dataset seaborn ha queste colonne utili. Riempiamo i NaN di deck con 'Unknown'
df['deck'] = df['deck'].astype(str).replace('nan', 'Unknown')

# Encoding: Trasformiamo testo in numeri (es. male/female -> 0/1)
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])
df['embarked'] = le.fit_transform(df['embarked'])
df['who'] = le.fit_transform(df['who'])
df['deck'] = le.fit_transform(df['deck'])

X = df[features]
y = df[target]

# Split Train/Test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Configurazione del modello XGBoost
xgb_model = XGBClassifier(
    n_estimators=500,      # Molti più alberi
    learning_rate=0.01,    # Learning rate molto basso per precisione estrema
    max_depth=5,           # Profondità media per catturare relazioni complesse
    gamma=0.1,             # Parametro di regolarizzazione
    subsample=0.8,         # Usa solo l'80% dei dati per ogni albero (riduce varianza)
    colsample_bytree=0.8,  # Usa solo l'80% delle feature per ogni albero
    reg_alpha=0.01,        # Regolarizzazione L1 (Lasso)
    use_label_encoder=False,
    eval_metric='logloss',
    random_state=42
)

# 3. Addestramento
print("Addestramento del modello in corso...")
xgb_model.fit(X_train, y_train)

# 4. Predizione
y_pred = xgb_model.predict(X_test)

# --- VISUALIZZAZIONE RISULTATI ---
plt.figure(figsize=(14, 6))

# Grafico 1: Matrice di Confusione
plt.subplot(1, 2, 1)
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix: Titanic (XGBoost)')
plt.xlabel('Predetto (0=Morto, 1=Sopravvissuto)')
plt.ylabel('Reale')

# Grafico 2: Feature Importance
# Vediamo quali fattori hanno influenzato di più la sopravvivenza
plt.subplot(1, 2, 2)
feat_importances = pd.Series(xgb_model.feature_importances_, index=features)
feat_importances.nlargest(10).plot(kind='barh', color='teal')
plt.title('Fattori più importanti per la sopravvivenza')
plt.xlabel('Importanza (F-Score)')

plt.tight_layout()
plt.show()

# Metriche finali
print(f"\nAccuratezza XGBoost: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nReport Tecnico:")
print(classification_report(y_test, y_pred))