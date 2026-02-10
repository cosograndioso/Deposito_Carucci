'''17.Esercizio 1:  Condizioni e cicli
Chieda all’utente di inserire un numero intero positivo. 
 
 Usi un ciclo for per stampare tutti i numeri da 1 fino al numero inserito. 
 
 Per ogni numero: 
 
 stampi "pari" se il numero è pari 
 
 stampi "dispari" se il numero è dispari 
 
 
 
 Se l’utente inserisce un numero minore o uguale a zero, il programma deve stampare un messaggio di errore.'''
 
 
while True:
    nPositivo= int (input("inserisci un numero positivo"))
    if(nPositivo>0):
        print("bravo e' positivo")
        break
    else:
        print("per favore inserire un numero positivo")
       
    
for i in range(1, nPositivo + 1):
        if i % 2 == 0:
            print(i, "pari")
        else:
            print(i, "dispari")



