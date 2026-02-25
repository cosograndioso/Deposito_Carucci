'''Pandas
Esercizio 1: Analisi Esplorativa dei Dati
Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati usando pandas.

Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su un gruppo di persone: Nome, Età, Città e Salario.

Caricare i dati in un DataFrame autogenerandoli casualmente.

Visualizzare le prime e le ultime cinque righe del DataFrame.

Visualizzare il tipo di dati di ciascuna colonna.

Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).

Identificare e rimuovere eventuali duplicati.

Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.

Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18 anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

Salvare il DataFrame pulito in un nuovo file CSV.'''


import pandas as pd
import numpy as np

data = {
    'Nome': ['Gabriele', 'Anna', 'Luca', 'Sara', 'Marco', 'Elena', 'Paolo', 'Giulia', 'Matteo', 'Chiara', 'Luca', 'Sara'],
    'Età': [25, 30, 17, 45, np.nan, 70, 12, 35, 28, np.nan, 17, 45], # Inseriti alcuni NaN per il punto 6
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Bari', 'Firenze', 'Roma', 'Milano', 'Napoli', 'Torino', 'Napoli', 'Torino'],
    'Salario': [2500, 3200, 0, 4100, 2900, np.nan, 0, 3500, 2700, 3100, 0, 4100]
}

df = pd.DataFrame(data)

print("--- Prime 5 righe ---")
print(df.head(5))
print("\n--- Ultime 5 righe ---")
print(df.tail(5))

print("\n--- Tipi di dati ---")
print(df.dtypes)

print("\n--- Statistiche descrittive ---")
statistiche = df[['Età', 'Salario']].agg(['mean', 'median', 'std'])
print(statistiche)

duplicati = df.duplicated().sum()
print(f"\nDuplicati trovati: {duplicati}")
df = df.drop_duplicates().reset_index(drop=True)

mediana_eta = df['Età'].median()
mediana_salario = df['Salario'].median()

df['Età'] = df['Età'].fillna(mediana_eta)
df['Salario'] = df['Salario'].fillna(mediana_salario)
print("\n--- Valori mancanti gestiti ---")

def classifica_eta(eta):
    if eta <= 18:
        return "Giovane"
    elif eta <= 65:
        return "Adulto"
    else:
        return "Senior"

df['Categoria Età'] = df['Età'].apply(classifica_eta)

df.to_csv("dataset_persone_pulito.csv", index=False)
print("\n--- File 'dataset_persone_pulito.csv' salvato con successo ---")

# Visualizzazione finale del risultato
print("\nDataFrame Finale:")
print(df)