'''lasse MembroSquadra:

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


from membroSquadra import Membro

class Allenatore(Membro):
    def __init__(self, nome: str, eta: int, anni_esp: int):
        
        super().__init__(nome, eta)
        self.anni_esp = anni_esp
        
    def dirige_allenamento(self, squadra): 
        print(f"L'allenatore {self.nome} sta dirigendo l'allenamento per i seguenti giocatori:")
        for g in squadra:
            print(f"- {g.nome} (Maglia n. {g.numero_maglia})")