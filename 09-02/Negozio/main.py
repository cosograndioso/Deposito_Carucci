


from utente import Utente
from inventario import inventario

def main():

    gestore = Utente()
    negozio = inventario()







    while True:
        print("\n=== SISTEMA GESTIONE NEGOZIO ===")
        print("1. Registrazione (Nuovo Cliente)")
        print("2. Login")
        print("3. Esci")
        
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            gestore.aggiungi_utente()
        
        elif scelta == "2":
            username, ruolo = gestore.login()
            
            if username: 
               
                if ruolo == "cliente":
                    while True:
                        print(f"\n--- MENU CLIENTE ({username}) ---")
                        print("1. Visualizza Articoli")
                        print("2. Acquista Articolo")
                        print("3. Visualizza i miei acquisti")
                        print("4. Logout")
                        sc = input("Scelta: ")
                        
                        if sc == "1":
                            negozio.visualizza_inventarioPerUtenti()
                        elif sc == "2":
                            gestore.compra(negozio, username)
                        elif sc == "3":
                            print(f"I tuoi acquisti: {gestore.utenti_db[username]['acquisti']}")
                        elif sc == "4":
                            break

                # --- MENU AMMINISTRATORE ---
                elif ruolo == "admin":
                    while True:
                        print("\n--- MENU AMMINISTRATORE ---")
                        print("1. Stato Inventario (Completo)")
                        print("2. Aggiungi Nuovo Prodotto")
                        print("3. Aggiorna Prodotto Esistente")
                        print("4. Rimuovi Prodotto")
                        print("5. Visualizza Guadagni Totali")
                        print("6. Logout")
                        sa = input("Scelta: ")
                        
                        if sa == "1":
                            negozio.visualizza_inventarioAmm()
                        elif sa == "2":
                            n = input("Nome: "); p = float(input("Prezzo: ")); q = int(input("Qta: "))
                            negozio.aggiungi_nuovo(n, p, q)
                        elif sa == "3":
                            n = input("Nome prodotto da modificare: ")
                            p = input("Nuovo prezzo (invio per saltare): ")
                            q = input("Nuova qta (invio per saltare): ")
                            negozio.aggiorna_prodotto(n, float(p) if p else None, int(q) if q else None)
                        elif sa == "4":
                            n = input("Nome prodotto da rimuovere: ")
                            negozio.rimuovi_prodotto(n)
                        elif sa == "5":
                            gestore.visualizza_guadagni()
                        elif sa == "6":
                            break
        
        elif scelta == "3":
            print("Chiusura sistema. Arrivederci!")
            break
        
        
if __name__ == "__main__":
    main()