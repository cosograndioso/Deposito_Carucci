'''Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
Attributi privati:
_numero (intero): il numero del posto.
_fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).
Metodi:
__init__(numero, fila): inizializza il posto impostando _occupato a False.
prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
Classi Derivate
PostoVIP:
Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
Metodi:
Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
PostoStandard:
Attributi aggiuntivi: costo  (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
Metodi:
Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
Classe Teatro
Attributi:
_posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
Metodi:
aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati.
'''

from teatro import Teatro
from vip import Vip, PostoStandard

def main():
    teatro = Teatro("Teatro sburrevolezza")
    
    
    teatro.aggiungi_posto(PostoStandard("1", "A", 10))
    teatro.aggiungi_posto(Vip("1", "V", 22, "Aperitivo e Lounge"))

    while True:
        print(f"\n--- GESTIONALE {teatro.nomeT.upper()} ---")
        print("1. Prenota un posto")
        print("2. Visualizza posti occupati")
        print("3. Aggiungi un nuovo posto alla sala")
        print("4. Esci")
        
        scelta = input("Seleziona opzione: ")

        if scelta == "1":
            f = input("Inserisci la fila (es. A o V): ").upper()
            n = input("Inserisci il numero: ")
            teatro.prenota_posto(f, n)
        
        elif scelta == "2":
            teatro.stampa_posti_occupati()

        elif scelta == "3":
            print("\n--- AGGIUNTA NUOVO POSTO ---")
            tipo = input("Tipo di posto (S per Standard, V per VIP): ").upper()
            fila = input("Lettera Fila: ").upper()
            numero = input("Numero Posto: ")
            
            try:
                costo = int(input("Costo del biglietto: "))
                
                if tipo == "V":
                    extra = input("Servizi extra inclusi: ")
                    nuovo_posto = Vip(numero, fila, costo, extra)
                else:
                    nuovo_posto = PostoStandard(numero, fila, costo)
                
                teatro.aggiungi_posto(nuovo_posto)
                print(f"Posto {fila}{numero} aggiunto correttamente!")
                
            except ValueError:
                print("Errore: Il costo deve essere un numero intero!")

        elif scelta == "4":
            print(f"Chiusura gestionale {teatro.nomeT}. Arrivederci!")
            break
        else:
            print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()
