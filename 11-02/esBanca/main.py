'''L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota).'''

from utenti import Utente
from admin import Admin
from contoBancario import Conto


database_admin = {
        "boss_admin": {"psw": "admin2024", "oggetto": Admin("Sofia", "Bianchi", "ADM-001")}
        }

database_utenti = {
    "mario88": {"psw": "12345", "oggetto": Utente("Mario", "Rossi")},
    "luca_verdi": {"psw": "segreto", "oggetto": Utente("Luca", "Verdi")}
}

def login():
    print("\n--- LOGIN SISTEMA BANCARIO ---")
    username = input("Username: ")
    password = input("Password: ")
    
    if username in database_admin and database_admin[username]["psw"] == password:
        return "ADMIN", database_admin[username]["obj"]
    
    
    if username in database_utenti and database_utenti[username]["psw"] == password:
        return "UTENTE", username # Restituiamo lo username per recuperare il conto dopo
    
    return None, None



def main():
    
    
    
    
    
    
    
    
    
    

    if __name__ == "__main__":
        main()