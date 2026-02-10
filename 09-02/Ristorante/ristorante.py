<<<<<<< HEAD
'''Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.'''

class Ristorante:
    
    aperto = False
    
    
    
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome  
        self.tipo_cucina = tipo_cucina
        self.menu = []
    
    def descrivi_ristorante(self):
        print(f"Ristorante: {self.nome} | Cucina: {self.tipo_cucina}")

    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è APERTO.")
        else:
            print(f"Il ristorante {self.nome} è CHIUSO.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è stato aperto!")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è stato chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        
        self.menu.append([piatto, prezzo])
        print(f"Aggiunto al menu: {piatto}")

    
    
    
    
    def togli_dal_menu_per_id(self, piatto_id):
        
        if 0 <= piatto_id < len(self.menu):
            rimosso = self.menu.pop(piatto_id)
            print(f"Rimosso: {rimosso[0]} (ID: {piatto_id})")
        else:
            print(f"L'ID {piatto_id} non esiste. Guarda il menu per gli ID corretti.")
            
    
    
    
    
    def stampa_menu(self):
        print(f"\n--- MENU {self.nome.upper()} ---")
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            
            for i in range(len(self.menu)):
                piatto = self.menu[i]
                print(f"ID: {i} | {piatto[0]} - {piatto[1]}€")

=======
'''Obiettivo: Creare una classe Ristorante che permetta di gestire alcune funzionalità di base .
Requisiti:
Definizione della Classe:
Creare una classe chiamata Ristorante.
La classe dovrebbe avere un costruttore __init__ che accetta due parametri: nome (nome del ristorante) e tipo_cucina (tipo di cucina offerta).
Definire un attributo aperto che indica se il ristorante è aperto o chiuso. Questo attributo deve essere impostato su False di default (cioè, il ristorante è chiuso).
Un Lista o + menu dove dentro ci sono i piatti e prezzi che ha il ristorante
Metodi della Classe:
descrivi_ristorante(): Un metodo che stampa una frase descrivendo il ristorante, includendo il nome e il tipo di cucina.
stato_apertura(): Un metodo che stampa se il ristorante è aperto o chiuso.
apri_ristorante(): Un metodo che imposta l'attributo aperto su True e stampa un messaggio che indica che il ristorante è ora aperto.
chiudi_ristorante(): Un metodo che imposta l'attributo aperto su False e stampa un messaggio che indica che il ristorante è ora chiuso.
aggiungi_al_menu(): Un metodo per aggiungere piatti al menu
togli_dal_menu(): Un metodo per togliere piatti al menu
stampa_menu(): Un metodo per stampare il menu
Testare la Classe:
Creare un'istanza della classe Ristorante, passando i valori appropriati al costruttore.
Testare tutti i metodi creati per assicurarsi che funzionino come previsto.'''

class Ristorante:
    
    aperto = False
    
    
    
    
    def __init__(self, nome, tipo_cucina):
        self.nome = nome  
        self.tipo_cucina = tipo_cucina
        self.menu = []
    
    def descrivi_ristorante(self):
        print(f"Ristorante: {self.nome} | Cucina: {self.tipo_cucina}")

    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} è APERTO.")
        else:
            print(f"Il ristorante {self.nome} è CHIUSO.")

    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è stato aperto!")

    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è stato chiuso.")

    def aggiungi_al_menu(self, piatto, prezzo):
        
        self.menu.append([piatto, prezzo])
        print(f"Aggiunto al menu: {piatto}")

    
    
    
    
    def togli_dal_menu_per_id(self, piatto_id):
        
        if 0 <= piatto_id < len(self.menu):
            rimosso = self.menu.pop(piatto_id)
            print(f"Rimosso: {rimosso[0]} (ID: {piatto_id})")
        else:
            print(f"L'ID {piatto_id} non esiste. Guarda il menu per gli ID corretti.")
            
    
    
    
    
    def stampa_menu(self):
        print(f"\n--- MENU {self.nome.upper()} ---")
        if not self.menu:
            print("Il menu è vuoto.")
        else:
            
            for i in range(len(self.menu)):
                piatto = self.menu[i]
                print(f"ID: {i} | {piatto[0]} - {piatto[1]}€")

>>>>>>> 6f3b5d4de2cb9070e3d73296676c9aa6e7fe97d1
