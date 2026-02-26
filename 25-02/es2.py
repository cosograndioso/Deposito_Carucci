'''Pandas
Esercizio 2: Manipolazione e Aggregazione dei Dati
Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con pandas.

Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.

Caricare i dati in un DataFrame.

Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra Quantità e Prezzo Unitario.

Raggruppare i dati per Prodotto e calcolare il totale delle vendite per ciascun prodotto.

Trovare il prodotto più venduto in termini di Quantità.

Identificare la città con il maggior volume di vendite totali.

Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo valore (es., 1000 euro).

Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente.

Visualizzare il numero di vendite per ogni città.'''



import pandas as pd

dati_vendite = {
    'Prodotto': ['Monitor', 'Tastiera', 'Mouse', 'Monitor', 'Laptop', 'Mouse', 'Tastiera', 'Laptop', 'Monitor'],
    'Quantità': [2, 5, 10, 1, 2, 15, 3, 1, 4],
    'Prezzo Unitario': [150, 30, 20, 150, 1200, 20, 35, 1250, 155],
    'Città': ['Milano', 'Roma', 'Napoli', 'Milano', 'Torino', 'Roma', 'Napoli', 'Milano', 'Torino']
}

df = pd.DataFrame(dati_vendite)



df.to_csv('vendite_output.csv', index=False)


def percorso():
    perc = pd.read_csv('vendite_output.csv')
    print("--- Contenuto del file CSV caricato ---")
    
    return perc




def stats():
    df = percorso()

    print("\n--- ELABORAZIONE STATISTICHE ---")
    tot= df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
    print("\n2. Totale vendite per prodotto:\n", tot)
    tot.to_csv("sdgfvdgs.csv", index=False)

    vendite_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
    print("\n3. Totale vendite per prodotto:\n", vendite_prodotto)

   
    top_quantita = df.groupby('Prodotto')['Quantità'].sum().idxmax()
    print(f"\n4. Prodotto più venduto (quantità): {top_quantita}")

    top_citta = df.groupby('Città')['Totale Vendite'].sum().idxmax()
    print(f"5. Città con maggior volume vendite: {top_citta}")

    
    df_mille = df[df['Totale Vendite'] > 1000]
    print("\n6. Vendite > 1000€:\n", df_mille)

   
    df.sort_values(by='Totale Vendite', ascending=False, inplace=True)
    print("\n7. DataFrame ordinato:\n", df)

    num_vendite_citta = df['Città'].value_counts()
    print("\n8. Numero di transazioni per città:\n", num_vendite_citta)







percorso()
stats()

'''
df ['tot_vendiite'] = df ['Prezzo Unitario'] * df ['Quantità']


vendite_per_prodotto = df.groupby('Prodotto')['tot_vendiite'].sum()
print("\n3. Totale vendite per prodotto:")
print(vendite_per_prodotto)

prodotto_top_quantita = df.groupby('Prodotto')['Quantità'].sum().idxmax()
print(f"\n4. Prodotto più venduto (quantità): {prodotto_top_quantita}")


citta_top_vendite = df.groupby('Città')['tot_vendiite'].sum().idxmax()
print(f"5. Città con maggior volume vendite: {citta_top_vendite}")


df_high_value = df[df['tot_vendiite'] > 1000].copy()
print("\n6. Vendite superiori a 1000€:")
print(df_high_value)


df.sort_values(by='tot_vendiite', ascending=False, inplace=True)
print("\n7. DataFrame ordinato per vendite (Decrescente):")
print(df)


conteggio_vendite_citta = df['Città'].value_counts()
print("\n8. Numero di transazioni per città:")
print(conteggio_vendite_citta)

df.to_csv('risultati_vendite.csv', index=False)


vendite_per_prodotto.to_csv('riepilogo_prodotti.csv')

print("\nFile CSV generati con successo!")
'''