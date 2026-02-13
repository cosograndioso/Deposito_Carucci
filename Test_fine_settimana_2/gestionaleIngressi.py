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
class GestionaleIngressi:
    def __init__(self, nome_azienda):
        self.nome_azienda = nome_azienda 
       
        self.__registro_accessi = [] #ovviamente incaspulate
        self.__registro_uscite = []

   
   
   
   
    
   
   
   
    def registra_ingresso(self, persona: Dipendente): # utlizzo della classe padre pe vedere le info di una persona e aggiungo la possibilita' di registrare entrata 
        dati_persona = persona.info() 
        self.__registro_accessi.append(dati_persona)
        print(f"[{self.nome_azienda}] Ingresso registrato per: {dati_persona}")

    
    def registra_uscite(self, persona: Dipendente): #stessa roba di prima ma con le uscite
        """
        ESEMPIO DI POLIMORFISMO:
        Il metodo accetta un oggetto di tipo 'Dipendente'. Grazie al polimorfismo, 
        Python chiamerà automaticamente la versione corretta di .info() 
        (quella della classe padre o quella specifica della classe Ruoli) 
        in base all'oggetto che viene effettivamente passato durante l'esecuzione.
        """
        
        
        dati_persona = persona.info() 
        self.__registro_uscite.append(dati_persona)
        print(f"[{self.nome_azienda}] uscita registrato per: {dati_persona}")
    
    
    def stampa_report(self, chi_lo_chiede): #mando a schermo entrate e uscite
        if chi_lo_chiede.calcola_privilegi() == "admin":
            print(f"\n--- REPORT RISERVATO PER: {chi_lo_chiede.Get_nome()} ---")
            for record in self.__registro_accessi:
                print(f"Entrata: {record}")
        else:
            print(f"\n[ERRORE] Accesso negato a {chi_lo_chiede.Get_nome()}. Solo gli Admin possono vedere il report.")
        
        
        
        
        for record in self.__registro_accessi:
            print(f"dati di entrate: {record}")
            
            
        for record2 in self.__registro_uscite:
            print(f"dati di uscite: {record2}")
            
        