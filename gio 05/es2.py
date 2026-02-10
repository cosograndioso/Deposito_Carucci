'''18.Esercizio 2:  Funzioni e Liste
Definisca una funzione chiamata conta_vocali. 
 
 La funzione deve: 
 
 ricevere una stringa come parametro 
 
 contare quante vocali contiene (a, e, i, o, u) 
 
 restituire il numero totale di vocali 
 
 
 
 Nel programma principale: 
 
 chiedi all’utente di inserire una parola 
 
 chiama la funzione 
 
 stampa il numero di vocali trovate '''
 
 

def conta_Vocali (parola):
    vocali = "aeiouAEIOU"
    count_Vocali=0
    for lettera in parola:
        if lettera in vocali:
            count_Vocali += 1
    return count_Vocali


while True:
    parola_utente = input("Inserisci una parola o solo q per uscire: ")
    
    if parola_utente=="q":
        break
    else:
        numero_vocali = conta_Vocali (parola_utente)
        print("La parola contiene", numero_vocali, "vocali.")
