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


from ristorante import Ristorante


if __name__ == "__main__":
    nome_rist = input("Inserisci il nome del tuo ristorante: ")
    tipo = input("Tipo di cucina: ")
    rist = Ristorante(nome_rist, tipo)

   
   
   
   
   
   
   
   
    while True:
        print(f"\n--- GESTIONALE {rist.nome.upper()} ---")
        print("1. Apri/Chiudi Ristorante")
        print("2. Aggiungi piatto al menu")
        print("3. Stampa Menu")
        print("4. apero o chiuso?")
        print("5. rimuovi piatti")
        
        print("6. Esci")        
        
        
        
        
        
        
        
        
        
        
        
        scelta = int (input("Cosa vuoi fare? "))

        if scelta == 1:
            if rist.aperto:
                rist.chiudi_ristorante()
            else:
                rist.apri_ristorante()
        elif scelta == 2:
            p = input("Nome piatto: ")
            pr = float(input("Prezzo: "))
            rist.aggiungi_al_menu(p, pr)
        elif scelta == 3:
            rist.stampa_menu()
        elif scelta == 4:
            
            rist.stato_apertura()
            
        elif scelta == 5:
            if not rist.menu:
                print("Il menu è già vuoto, non c'è nulla da rimuovere!")
            else:
                rist.stampa_menu() 
                id_da_rimuovere = int(input("Inserisci l'ID del piatto da rimuovere: "))
                rist.togli_dal_menu_per_id(id_da_rimuovere)
        
        
        
        elif scelta == 6:
            print("buonagiornata")    
            break
            
            
            
            
        

