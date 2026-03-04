import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import optuna
import xgboost as xgb
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
import seaborn as sns
from sklearn.datasets import fetch_openml



df = sns.load_dataset('diamonds')


print(f"Dimensione iniziale: {df.shape}")
print(f"Duplicati iniziali: {df.duplicated().sum()}")


df = df.drop_duplicates()


df = df[(df[['x', 'y', 'z']] != 0).all(axis=1)]

# --- Feature Engineering ---
# Creiamo feature derivate che hanno senso per il settore dei diamanti.
# Volume: una stima della grandezza fisica (x*y*z).
df['volume'] = df['x'] * df['y'] * df['z']
# Densità: data dal rapporto tra peso (carat) e volume. È utile per scovare anomalie.
# Se un diamante ha una densità anomala, potrebbe essere un errore di inserimento dati.
df['density'] = df['carat'] / df['volume']

# Rapporto Lunghezza/Larghezza (L/W Ratio):
# Indica la simmetria. Per i diamanti rotondi, dovrebbe essere vicino a 1.
df['l_w_ratio'] = df['x'] / df['y']

# Relazione geometrica tra profondità e tavola (proporzioni del taglio)
df['depth_table_ratio'] = df['depth'] / df['table']

# Mappatura manuale (Ordinal Encoding) per preservare l'ordine di qualità.
# Questo riduce drasticamente l'errore perché i numeri ora hanno un senso logico (0=peggiore, max=migliore).
cut_map = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
color_map = {'J': 0, 'I': 1, 'H': 2, 'G': 3, 'F': 4, 'E': 5, 'D': 6}
clarity_map = {'I1': 0, 'SI2': 1, 'SI1': 2, 'VS2': 3, 'VS1': 4, 'VVS2': 5, 'VVS1': 6, 'IF': 7}

# Forziamo la conversione a 'int' dopo la mappatura. Questo assicura che le colonne
# non siano più di tipo 'category', risolvendo l'errore di XGBoost.
df['cut'] = df['cut'].map(cut_map).astype(int)
df['color'] = df['color'].map(color_map).astype(int)
df['clarity'] = df['clarity'].map(clarity_map).astype(int)





print("\n--- Dopo la pulizia ---")
print(df.head())
print(f"Dimensione finale: {df.shape}")

X = df.drop('price', axis=1)
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



def objective(trial):
    param = {


    'tree_method':'hist',
    'enable_categorical':True,
    'n_estimators': trial.suggest_int('n_estimators', 500, 1000, step=100),
    'learning_rate': trial.suggest_float('learning_rate', 0.001, 0.1, log=True),
    'max_depth': trial.suggest_int('max_depth', 3, 12),
    'subsample': trial.suggest_float('subsample', 0.5, 1.0),
    'colsample_bytree': trial.suggest_float('colsample_bytree', 0.5, 1.0),
    'gamma': trial.suggest_float('gamma', 0, 5),
    'reg_alpha': trial.suggest_float('reg_alpha', 0, 5),
    # Parametri fissi
    'n_jobs': -1,
    'random_state': 42
    

    }     


    # tree_method='hist', enable_categorical=True
    model = xgb.XGBRegressor(**param)
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    
    # Cross-Validation basata su R2
    score = cross_val_score(model, X_train, y_train, cv=kf, scoring='r2').mean()
    return score



print("pulizia in sesso")

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100,  show_progress_bar=True)

print("\n--- Ottimizzazione completata ---")
print(f"Migliori parametri trovati: {study.best_params}")

# Creiamo il modello finale usando i parametri MIGLIORI trovati da Optuna
# Usiamo il nome 'xgb_model' così il resto dello script (grafici, metriche) funziona senza modifiche
xgb_model = xgb.XGBRegressor(**study.best_params, tree_method='hist', enable_categorical=True, random_state=42, n_jobs=-1)

print("Addestramento del modello in corso...")
xgb_model.fit(X_train, y_train)

# 4. Predizione
y_pred = xgb_model.predict(X_test)

# --- VISUALIZZAZIONE RISULTATI ---
plt.figure(figsize=(14, 6))

# Grafico 1: Scatter Plot (Reale vs Predetto)
plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5, color='purple')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2) # Linea ideale
plt.title('Prezzo Reale vs Predetto (XGBoost)')
plt.xlabel('Prezzo Reale ($)')
plt.ylabel('Prezzo Predetto ($)')

# Grafico 2: Feature Importance
plt.subplot(1, 2, 2)
feat_importances = pd.Series(xgb_model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh', color='mediumpurple')



plt.title('Fattori che influenzano il prezzo')
plt.xlabel('Importanza')

plt.tight_layout()
plt.show()

# --- GRAFICO DEI RESIDUI ---
# Un buon modello ha residui (errori) distribuiti casualmente attorno allo zero.
# Se ci sono dei pattern (es. a forma di imbuto), significa che il modello ha dei bias.
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.5, color='green')
plt.axhline(y=0, color='r', linestyle='--') # Linea dello zero, l'ideale
plt.title('Grafico dei Residui (Reale - Predetto)')
plt.xlabel('Prezzo Predetto ($)')
plt.ylabel('Residui ($)')
plt.show()

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nErrore Medio (RMSE): ${np.sqrt(mse):.2f}")
print(f"Accuratezza (R2 Score): {r2 * 100:.2f}%")
