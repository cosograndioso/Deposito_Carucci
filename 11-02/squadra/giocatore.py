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
class Giocatore(Membro):
    def __init__(self,nome:str,eta:int,ruolo:str,numero_maglia:int):
        super().__init__(nome, eta) 
        
        
        
        self.ruolo=ruolo
        self.numero_maglia=numero_maglia
        
        
    def gioca_partita(self,tattica:str):
        
        print(f"Il giocatore {self.nome} con il numero {self.numero_maglia} "
              f"sta giocando come {self.ruolo} seguendo la tattica: {tattica}")
         
    