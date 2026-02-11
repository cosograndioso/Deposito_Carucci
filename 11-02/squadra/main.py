'''classe MembroSquadra:

Attributi:
nome (stringa)
età (intero)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra)
Classi Derivate:

Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore
Allenatore:
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro'''

import random
from membroSquadra import Membro
from giocatore import Giocatore
from allenatore import Allenatore
from assistente import Assistente

def simulazione_partita(squadra1, nome1, squadra2, nome2):
    print(f"\n---  MATCH DAY: {nome1} vs {nome2} ---")
    print("Le squadre entrano in campo...")
    
    
    gol1 = random.randint(0, 5)
    gol2 = random.randint(0, 5)
    
    print("-" * 30)
    print(f"RISULTATO FINALE: {nome1} {gol1} - {gol2} {nome2}")
    print("-" * 30)
    
    if gol1 > gol2:
        print(f" VINCITORE: {nome1}!")
    elif gol2 > gol1:
        print(f" VINCITORE: {nome2}!")
    else:
        print(" PAREGGIO! Si decide ai rigori... ma questa è un'altra storia.")

def main():
    
    mister_a = Allenatore("Ancelotti", 64, 30)
    assistente_a = Assistente("Pintus", 61, "Preparatore Atletico")
    giocatori_a = [
        Giocatore("Vinicius", 23, "Attaccante", 7),
        Giocatore("Bellingham", 20, "Centrocampista", 5)
    ]
    
   
    mister_b = Allenatore("Guardiola", 53, 20)
    assistente_b = Assistente("Planchart", 50, "Analista Video")
    giocatori_b = [
        Giocatore("Haaland", 23, "Punta", 9),
        Giocatore("De Bruyne", 32, "Regista", 17)
    ]

    while True:
        print("\n" + "="*30)
        print("   GESTIONALE SQUADRE CALCIO   ")
        print("="*30)
        print("1. Mostra Staff & Rosa (Squadra A)")
        print("2. Mostra Staff & Rosa (Squadra B)")
        print("3. Allenamento & Supporto (Squadra A)")
        print("4. GIOCA PARTITA ")
        print("5. Esci")
        
        scelta = input("\nSeleziona un'opzione: ")

        if scelta == "1":
            print("\n--- INFO SQUADRA A ---")
            print("[Allenatore]")
            mister_a.descrivi()
            print("[Assistente]")
            assistente_a.descrivi()
            print("[Giocatori]")
            for g in giocatori_a:
                g.descrivi()
        
        elif scelta == "2":
            print("\n--- INFO SQUADRA B ---")
            print("[Allenatore]")
            mister_b.descrivi()
            print("[Assistente]")
            assistente_b.descrivi()
            print("[Giocatori]")
            for g in giocatori_b:
                g.descrivi()

        elif scelta == "3":
            print("\n--- FASE DI PREPARAZIONE ---")
            
            assistente_a.supporta_team()
            
          
            tattica = input("\nChe tattica deve usare l'allenatore? ")
            mister_a.dirige_allenamento(giocatori_a)
            for g in giocatori_a:
                g.gioca_partita(tattica)

        elif scelta == "4":
            
            assistente_a.supporta_team()
            assistente_b.supporta_team()
            simulazione_partita(giocatori_a, "Real Madrid", giocatori_b, "Manchester City")

        elif scelta == "5":
            print("\n addio bastardo")
            break
        else:
            print("\n Opzione non valida! Riprova.")

if __name__ == "__main__":
    main()