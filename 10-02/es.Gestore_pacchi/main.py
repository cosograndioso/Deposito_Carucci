'''Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.'''



from pacco import Pacco
from magazzino import Magazzino
from gestore import GestorePacchi


if __name__ == "__main__":

    mag = Magazzino()
    mag.aggiungiPacco(1, Pacco("PC", 5, True))
    mag.aggiungiPacco(2, Pacco("Vestiti", 15, False))
    mag.aggiungiPacco(3, Pacco("Monitor", 8, True))
    mag.aggiungiPacco(4, Pacco("Stampante", 7, True))
    mag.aggiungiPacco(5, Pacco("Libri", 10, False))


    gestore = GestorePacchi(mag)

    while True:
        print("\n--- Menu ---")
        print("1 - Visualizza tutti i pacchi")
        print("2 - Visualizza pacchi in magazzino")
        print("3 - Visualizza pacchi in consegna")
        print("4 - Cambia stato pacco")
        print("5 - Mostra peso totale pacchi non consegnati")
        print("0 - Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == "1":
            mag.visualizzaMagazzino()
        elif scelta == "2":
            mag.visualizzaMagazzino("in magazzino")
        elif scelta == "3":
            mag.visualizzaMagazzino("in consegna")
        elif scelta == "4":
            pacco_id = int(input("Inserisci ID pacco da aggiornare: "))
            print("1 - In magazzino")
            print("2 - In consegna")
            print("3 - Consegnato")
            stato_scelta = input("Scegli stato: ")
            if stato_scelta == "1":
                gestore.magazzino.cambiaStatoPacco(pacco_id, "in magazzino")
            elif stato_scelta == "2":
                gestore.mettiInConsegna(pacco_id)
            elif stato_scelta == "3":
                gestore.segnalaConsegnato(pacco_id)
            else:
                print("Scelta non valida")
        elif scelta == "5":
            peso_totale = gestore.pesoTotaleNonConsegnati()
            print("Peso totale pacchi non consegnati:", peso_totale, "kg")
        elif scelta == "0":
            print("Uscita dal programma...")
            break
        else:
            print("Scelta non valida")







