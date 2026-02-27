'''Esercizio: Analisi delle Vendite "TechStore"
Obiettivo: Generare un set di dati fittizio di vendite, pulirlo, analizzarlo ed estrarre insight visivi utilizzando lo stack Python per la Data Science.

Step 1: Generazione dei Dati (NumPy)
Importa la libreria numpy.

Genera un array di 200 ID prodotto univoci (da 1 a 200).

Crea un array di Prezzi contenente 200 numeri decimali casuali compresi tra 10.0 e 500.0 (usa np.random).

Crea un array di Quantità Vendute contenente 200 numeri interi casuali compresi tra 1 e 50.

Calcola un nuovo array Ricavi moltiplicando l'array dei Prezzi per quello delle Quantità Vendute sfruttando il calcolo vettoriale di NumPy.

Step 2: Costruzione e Pulizia del Dataset (Pandas)
Importa la libreria pandas.

Crea un DataFrame unendo gli array creati nello Step 1 (colonne: ID_Prodotto, Prezzo, Quantita, Ricavo).

Aggiungi una nuova colonna chiamata Categoria assegnando casualmente a ogni riga una di queste stringhe: ['Elettronica', 'Accessori', 'Software', 'Periferiche']. (Suggerimento: usa np.random.choice).

Manipolazione: Introduci intenzionalmente 10 valori nulli (NaN) nella colonna Quantita.

Pulizia: Trova le righe con valori nulli e riempile (fillna) con il valore mediano della colonna Quantita. Aggiorna di conseguenza la colonna Ricavo per quelle righe.

Step 3: Analisi dei Dati (Pandas)
Mostra le statistiche descrittive generali del DataFrame (media, min, max, ecc.).

Utilizza il metodo groupby per calcolare il Ricavo Totale per ogni Categoria.

Filtra il DataFrame per mostrare solo i prodotti che hanno generato un ricavo superiore a 10.000€.

Ordina il DataFrame in base al Ricavo in ordine decrescente e mostra i "Top 5" prodotti.

Step 4: Visualizzazione Grafica (Matplotlib / Seaborn)
Importa matplotlib.pyplot e (opzionalmente) seaborn.

Grafico 1 (Bar Plot): Crea un grafico a barre che mostri il Ricavo Totale per ogni Categoria (basato sul raggruppamento dello Step 3). Aggiungi titolo, etichette agli assi e colori.

Grafico 2 (Scatter Plot): Crea un grafico a dispersione (scatter plot) che mostri la relazione tra Prezzo (asse X) e Quantita (asse Y). Colora i punti in base alla Categoria.

Grafico 3 (Box Plot): Crea un box plot per visualizzare la distribuzione dei Prezzi all'interno di ciascuna Categoria, per identificare eventuali outlier.'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# Step 1: Generazione dei Dati (NumPy)
# ==========================================
# Genera un array di 200 ID prodotto univoci (da 1 a 200).
id_prodotti = np.arange(1, 201)

# Crea un array di Prezzi contenente 200 numeri decimali casuali compresi tra 10.0 e 500.0.
prezzi = np.random.uniform(10.0, 500.0, 200)

# Crea un array di Quantità Vendute contenente 200 numeri interi casuali compresi tra 1 e 50.
quantita_vendute = np.random.randint(1, 51, 200)

# Calcola un nuovo array Ricavi.
ricavi = prezzi * quantita_vendute


# ==========================================
# Step 2: Costruzione e Pulizia del Dataset (Pandas)
# ==========================================
df = pd.DataFrame({
    "ID_Prodotto": id_prodotti,
    "Prezzo": prezzi,
    "Quantita": quantita_vendute,
    "Ricavo": ricavi
})

# Aggiungi Categoria
categorie = ['Elettronica', 'Accessori', 'Software', 'Periferiche']
df['Categoria'] = np.random.choice(categorie, size=len(df))

# Introduci intenzionalmente 10 valori nulli (NaN)
nan_indices = np.random.choice(df.index, size=10, replace=False)    
df.loc[nan_indices, 'Quantita'] = np.nan

# Pulizia valori nulli e ricalcolo ricavo
mediana_quantita = df['Quantita'].median()
df['Quantita'] = df['Quantita'].fillna(mediana_quantita) # Metodo moderno senza inplace
df['Ricavo'] = df['Prezzo'] * df['Quantita']

# ---> SALVATAGGIO DEL DATASET PRINCIPALE (Ora è nel posto corretto!) <---
df.to_csv('vendite_techstore_pulito.csv', index=False)
print("Dati principali salvati con successo in 'vendite_techstore_pulito.csv'!\n")


# ==========================================
# Step 3: Analisi dei Dati (Pandas)
# ==========================================
print("--- Statistiche Descrittive ---")
statistiche = df.describe()
print(statistiche)
# (Opzionale) Salva le statistiche in un CSV a parte
statistiche.to_csv('report_statistiche.csv') 

print("\n--- Ricavo Totale per Categoria ---")
ricavo_totale_per_categoria = df.groupby('Categoria')['Ricavo'].sum()
print(ricavo_totale_per_categoria)

print("\n--- Prodotti con Ricavo Alto (> 10.000€) ---")
prodotti_ricavo_alto = df[df['Ricavo'] > 10000]
print(prodotti_ricavo_alto)

print("\n--- Top 5 Prodotti per Ricavo ---")
top_5_prodotti = df.sort_values(by='Ricavo', ascending=False).head(5)
print(top_5_prodotti)
# (Opzionale) Salva la classifica in un CSV a parte
top_5_prodotti.to_csv('report_top_5_prodotti.csv', index=False)


# ==========================================
# Step 4: Visualizzazione Grafica (Matplotlib / Seaborn)
# ==========================================
# Grafico 1: Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x=ricavo_totale_per_categoria.index, y=ricavo_totale_per_categoria.values, palette='viridis')
plt.title('Ricavo Totale per Categoria')
plt.xlabel('Categoria')
plt.ylabel('Ricavo Totale (€)')
plt.show()

# Grafico 2: Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Prezzo', y='Quantita', hue='Categoria', palette='viridis')
plt.title('Relazione tra Prezzo e Quantità Venduta')
plt.xlabel('Prezzo (€)')
plt.ylabel('Quantità Venduta')
plt.legend(title='Categoria')
plt.show()

# Grafico 3: Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='Categoria', y='Prezzo', palette='viridis')
plt.title('Distribuzione dei Prezzi per Categoria')
plt.xlabel('Categoria')
plt.ylabel('Prezzo (€)')
plt.show()