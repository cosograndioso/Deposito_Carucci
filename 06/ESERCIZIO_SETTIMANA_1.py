'''Es riassuntivo prt 1
Hai 60 min per creare un esercizio
che rappresenti tutto quello che
hai imparato nella settimana
precedente, riprendi la tabella
delle conoscenze per maggiori info. 
Es riassuntivo prt 2
Andiamo ora a creare un sistema di
funzioni che richiami tutte le
singole parti che abbiamo creato nel
precedente esercizio, devono essere
usate SOLO funzioni e almeno da 2
decoratori ed essere ripetibile.
'''
'''Dovrai creare un sistema che gestisce un archivio di libri, applica sconti dinamici e genera un report finale. Il tutto deve essere orchestrato da una funzione principale 
"protetta" dai tuoi decoratori.'''


listUtenti=[]

biblioteca = [
    {"id": 1,"titolo": "Il Signore degli Anelli", "autore": "Tolkien", "prezzo": 25, "genere": "Fantasy", "anno": 1954},
    {"id": 2,"titolo": "1984", "autore": "Orwell", "prezzo": 15, "genere": "Distopia", "anno": 1949},
    {"id": 3,"titolo": "Il Problema dei 3 Corpi", "autore": "Liu Cixin", "prezzo": 20, "genere": "Sci-Fi", "anno": 2008}
]


def registrazione():
    id=1

    while True:

        nome = input("inserisci il nome").lower()
        
        cognome = input("inserisci il cognome").lower()
        
        utente = (id,nome,cognome)
        listUtenti.append(utente)
        
        print(f"utente {nome} registrato con id {id}")
        id+=1
        break
       
        
            



def accedi():
    while True:
        idR = int(input("inserisci id per accedere: "))
        
        for utentein in listUtenti:
            if utentein[0] == idR:
                print(f"utente trovato benvenuto {utentein[1]} {utentein[2]}")
                return 
        
        
            
        print("ID non trovato, devi prima registrarti.")
        registrazione()
                
        
    
        
        
        




def avviso_acquisto(funzione):
    def wrapper():
        funzione()
        
        while True:
            scelta = int(input("\nInserisci l'ID del libro per acquistarlo (o '0' per finire): "))
            
            if scelta == 0:
                print("Uscita dal sistema di acquisto. Grazie!")
                break
            
            trovato = False
            for p in biblioteca:
                if p["id"] == scelta:
                    trovato = True
                    tit = p["titolo"]
                    costo = p["prezzo"] 
                    
                    if p["anno"] <= 1949:
                        scont = 5
                        prezzo_finale = costo - scont  
                        print(f" {tit} acquistato per {prezzo_finale}$ (Sconto di {scont}$ applicato!)")
                    else:
                        print(f" {tit} acquistato a prezzo pieno per {costo}$")
                    
                    break 
            
            if not trovato:
                print("Libro non trovato. Riprova.")
                
    return wrapper






@avviso_acquisto
def mostra_catalogo():
    print("\n--- ELENCO DISPONIBILITÀ ---")
    for i, libro in enumerate(biblioteca):
        id_lib = libro["id"]
        titolo = libro["titolo"]
        autore = libro["autore"]
        prezzo = libro["prezzo"]
        genere= libro["genere"]
        anno= libro["anno"]
        print(f"{id_lib}. {titolo} - {autore} (prezzo:{prezzo}$- genere: {genere} - anno: {anno})")

   
    print("----------------------------")
        

print("--------------------")
print("benvenuto al mercaDioP")
print("--------------------")

while True:
    decisione = int(input("\nciao vuoi 1:registrati o 2:accedere o 0:per uscire: "))

    if decisione == 0:
        print("arrivederci")
        break
    
    elif decisione == 1:
        print("perfetto registrati inserendo i dati che richiedo")
        registrazione()
        
    elif decisione == 2:
        accedi()
        print("--------------------")
        print("bentornato al mercaDioP")
        print("--------------------")
        
        
        compraoNo = input("vuoi visualizzare il catalogo e acquistare? s o n: ").lower()
    
        match compraoNo:
            case "s":
                mostra_catalogo()
            case "n":
                print("buona giornata")
            case _:
                print("errore di battitura")
                   

       