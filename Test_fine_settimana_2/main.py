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


'''from dipendente import Dipendente
from ruoli import Ruoli
from gestionaleIngressi import GestionaleIngressi


azienda = GestionaleIngressi("Innovatech S.p.A.")


operaio = Dipendente("Marco", "Neri", 501)
direttore = Ruoli("Anna", "Bianchi", 100, "Direttore Generale")

# 3. Simulazione della giornata (Polimorfismo)
azienda.registra_ingresso(operaio)
azienda.registra_ingresso(direttore)



azienda.registra_uscite(operaio)



azienda.stampa_report()1
'''

from ruoli import Ruoli
from gestionaleIngressi import GestionaleIngressi










azienda = GestionaleIngressi("Deposito Carucci")


print("="*40)
print("     ACCESSO AL SISTEMA GESTIONALE")
print("="*40)


nome_log = input("Inserisci Nome: ")
ruolo_log = input("Inserisci Ruolo (admin/operatore): ").lower().strip()


user_sessione = Ruoli(nome_log, "carucci", 0, ruolo_log)

while True:
   
    
    privilegi = user_sessione.calcola_privilegi()
    
    print(f"AZIENDA: {azienda.nome_azienda}")
    print(f"UTENTE: {user_sessione.Get_nome()} | RUOLO: {user_sessione.Get_ruolo()}")
    print(f"LIVELLO ACCESSO: {privilegi}")
    
    print("1. [TUTTI] Registra INGRESSO")
    print("2. [TUTTI] Registra USCITA")
    print("3. [ADMIN] Visualizza REPORT COMPLETO")
    print("4. [LOGOUT] Cambia Utente")
    print("5. Esci")
    

    scelta = input("Seleziona operazione: ")

    if scelta == "1":
        print("\n--- NUOVO INGRESSO ---")
        n = input("Nome: ")
        c = input("Cognome: ")
        b = int(input("Badge: "))
        r = input("Ruolo: ")
        nuovo = Ruoli(n, c, b, r)
        azienda.registra_ingresso(nuovo)
        input("\nOperazione completata. Premi Invio...")

    elif scelta == "2":
        print("\n--- NUOVA USCITA ---")
        n = input("Nome: ")
        c = input("Cognome: ")
        b = int(input("Badge: "))
        r = input("Ruolo: ")
        nuovo = Ruoli(n, c, b, r)
        azienda.registra_uscite(nuovo)
        input("\nOperazione completata. Premi Invio...")

    elif scelta == "3":
       
        if user_sessione.calcola_privilegi() == "Accesso Totale":
            azienda.stampa_report(user_sessione)
        else:
            print("\n ACCESSO NEGATO!")
            print(f"Spiacente {user_sessione.Get_nome()}, solo gli Admin possono visualizzare i report.")
        

    elif scelta == "4":
        
        n = input("\nNuovo Nome: ")
        r = input("Nuovo Ruolo (admin/operatore): ").lower().strip()
        user_sessione = Ruoli(n, "Sistema", 0, r)
        print("Login effettuato con successo!")
        

    elif scelta == "5":
        print("\nSpegnimento... Arrivederci!")
        break