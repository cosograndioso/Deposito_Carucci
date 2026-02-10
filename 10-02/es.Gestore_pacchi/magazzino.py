'''Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero) e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati.'''




class Magazzino:
    def __init__(self):
        self.pacchi = {}  

    def aggiungiPacco(self, pacco_id, pacco):
        self.pacchi[pacco_id] = pacco

    def visualizzaMagazzino(self, stato=None):
        print("Elenco pacchi:")
        for id_pacco, pacco in self.pacchi.items():
            if stato is None or pacco.stato == stato:
                pacco.info()

    def cambiaStatoPacco(self, pacco_id, nuovo_stato):
        if pacco_id in self.pacchi:
            self.pacchi[pacco_id].cambiaStato(nuovo_stato)
            print(f"Pacco {self.pacchi[pacco_id].codice} aggiornato a '{nuovo_stato}'")
        else:
            print("Pacco non trovato")

                
        
        
        
       
                
    
