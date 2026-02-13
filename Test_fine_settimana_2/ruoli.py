'''ES COMPLESSIVO - Esercizio di TEST - Gestionale per l’Ingresso a Lavoro (OOP completo)

In una cartella specifica della tua repository (ad esempio: /progetti/OOP_GestionaleIngressoLavoro), realizza insieme al tuo gruppo un gestionale per l’ingresso a lavoro (accesso dipendenti, badge, turni, ecc.) utilizzando la programmazione ad oggetti.

Obiettivo generale:
Progettare e implementare un piccolo sistema software che gestisca la logica di ingresso in azienda (ad esempio persone, ruoli, badge, turni, controlli di accesso, log di entrata/uscita, ecc.), usando in modo evidente tutte e quattro le regole principali dell’OOP:

Astrazione

Ereditarietà

Incapsulamento

Polimorfismo

Il progetto dovrà:

essere organizzato nella cartella indicata all’interno della vostra repository;

contenere più file e/o moduli coerenti con l’idea di “gestionale per l’ingresso a lavoro”;

mostrare chiaramente, nel codice e nella struttura, dove e come vengono applicate le quattro regole OOP.

Non ci sono altre specifiche obbligatorie: siete voi a dover definire quali oggetti esistono, come interagiscono, quali responsabilità hanno e come dimostrare in modo chiaro l’uso di astrazione, ereditarietà, incapsulamento e polimorfismo.'''


from dipendente import Dipendente
class Ruoli (Dipendente):
    def __init__(self, nome, cognome, id_badge, ruolo):
        super().__init__(nome, cognome, id_badge)
        
        self.__ruolo=ruolo
        
    def Get_ruolo(self):
        return self.__ruolo

    def Set_ruolo(self, nuovo_ruolo):
        self.__ruolo = nuovo_ruolo
        
    def aggiorna_ruolo(self, nRuolo):    
     self.Set_ruolo(nRuolo)
     print(f"Ruolo aggiornato a: {self.__ruolo}")
     
     
    def calcola_privilegi(self):
        if self.__ruolo.lower() == "admin":
            return "Accesso Totale"
        return "Accesso Standard "
     
    def info(self):
        # super().info() recupera la stringa "Dipendente: Mario Rossi | Badge: 101", cosi sfrutto il padre 
        
        return f"{super().info()} | Ruolo: {self.Get_ruolo()}" 
     
        
        