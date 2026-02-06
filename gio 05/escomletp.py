'''Esercizio Completo

Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero, il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.'''


listadiU=[]
verifica = True
while verifica:
    nP = int(input("Inserisci un numero positivo cazzo: "))
    listadiU.append(nP)
    if nP > 0:
        break
    else:
        print("Il numero dev essere positiv")
        verifica = False  
sommaP=0
for i in range(1, nP + 1):
    
    
    
    if i % 2 == 0:
    
        sommaP += i

print("Somma numeri pari:", sommaP)    



for i in range(1, nP + 1):
    if i % 2 != 0:
        print(i)
        
    
primo=True    
if nP < 2:
    primo = False
    
else:
    for i in range(2, int(nP**0.5) + 1):
        if nP % i == 0:
            primo = False
            break
        
if primo:
   print(f"{nP} è un numero primo")
else:
    print(f"{nP} NON è un numero primo dio bono")
    
    
    
while True:
    scelta = input("Vuoi (v)isualizzare la lista dei tentativi?  m modifica (q per uscire): ").lower()

    if scelta == "v":
        print("Lista tentativi:", listadiU)
    
    
    elif scelta=="m":
        try:
            indice = int(input("Inserisci l'indice del numero da modificare (0 è il primo): "))
            nuovo_valore = int(input("Inserisci il nuovo numero: "))
            listadiU[indice] = nuovo_valore
            print("Lista aggiornata:", listadiU)
        except (ValueError, IndexError):
            print("Errore: indice non valido o valore non intero")
    
    elif scelta == "q":
        print("Programma terminato.")
        break
    
    else:
        print("Scelta non valida, riprova")