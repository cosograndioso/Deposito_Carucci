'''Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti, gestire l'inventario e permettere agli amministratori di supervisionare le operazioni. Il sistema sarà strutturato in tre parti principali:

Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.

Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).

Amministrazione:
l'analisi del negozio da parte degli amministratori.Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione, nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori.'''


class Utente:
    def __init__(self):
        
        self.utenti_db = {
            "admin": {"password": "123", "ruolo": "admin"}
        }
        acquisti =[]
    def aggiungi_utente(self):
            
        username = input("Scegli un username: ")
        password = input("Scegli una password: ")
        
        if username in self.utenti_db:
            print("Username già occupato!")
        else:
            
            self.utenti_db[username] = {
                "password": password, 
                "ruolo": "cliente", 
                "acquisti": []
            }
            print(f"Utente {username} creato con successo!")
            
            
    def login(self):
        user = input("Username: ")
        psw = input("Password: ")
        
        
        if user in self.utenti_db and self.utenti_db[user]["password"] == psw:
            ruolo = self.utenti_db[user]["ruolo"]
            print(f"\nLogin effettuato! Benvenuto {user} ({ruolo})")
            return user, ruolo  
        else:
            print("\nCredenziali errate!")
            return None, None
        
        
        
    def compra(self):
            
        pass
    
    
    
    
    
    #po0ter acquistare 
    
    #tenere traccia degli acquisti e acquistare 
    #vedere guadagnop tatale totali 
    
    
    
        