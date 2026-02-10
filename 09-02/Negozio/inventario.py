'''Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:

Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.

Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).   FATTO

Amministrazione:
l'analisi del negozio da parte degli amministratori.Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione, nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori.'''

class inventario:
    def __init__(self):
        self.magazzino = {
            "Laptop": {"prezzo": 850.00, "quantita": 10},
            "Mouse Wireless": {"prezzo": 25.50, "quantita": 50},
            "Tastiera Meccanica": {"prezzo": 70.00, "quantita": 15},
            "Monitor 24 pollici": {"prezzo": 150.00, "quantita": 8},
            "Cuffie Bluetooth": {"prezzo": 45.90, "quantita": 25}
        }
    
      
    
    
    
    
    
    
    def visualizza_inventarioAmm(self):
        for prodotto, info in self.magazzino.items():
            print(f"Prodotto: {prodotto} | Prezzo: {info['prezzo']}€ | Qta: {info['quantita']}")
            
    def visualizza_inventarioPerUtenti(self):
        for prodotto, info in self.magazzino.items():
            print(f"Prodotto: {prodotto} | Prezzo: {info['prezzo']}€ ")    
            
            
               
    def aggiorna_prodotto(self,nome, nuovo_prezzo=None, nuova_qta=None):
        if nome in self.magazzino:
            if nuovo_prezzo is not None:
                self.magazzino[nome]["prezzo"] = nuovo_prezzo
            if nuova_qta is not None:
                self.magazzino[nome]["quantita"] = nuova_qta
            print(f"Prodotto '{nome}' aggiornato correttamente.")
        else:
            print("Errore: Prodotto non trovato.")
            
            
    def aggiungi_nuovo(self, nome, prezzo, qta):
        """Aggiunge una nuova chiave al dizionario"""
        self.magazzino[nome] = {"prezzo": prezzo, "quantita": qta}
        print(f"'{nome}' inserito in inventario.")

    def rimuovi_prodotto(self, nome):
        """Elimina una chiave dal dizionario"""
        if nome in self.magazzino:
            del self.magazzino[nome]
            print(f"'{nome}' rimosso dal sistema.")
            
            
    
    def acquista(self):
        scelta = input("\nCosa desideri acquistare? ")
        if scelta in self.magazzino:
            
            if self.magazzino[scelta]["quantita"] > 0:
                self.magazzino[scelta]["quantita"] -= 1 # Togliamo un pezzo
                prezzo = self.magazzino[scelta]["prezzo"]
                print(f"Hai acquistato {scelta} con successo!")
                return prezzo 
            else:
                print("Spiacenti, articolo esaurito!")
                return None
        else:
            print("Articolo non trovato in inventario.")
            return None

             
            
            
            
            
