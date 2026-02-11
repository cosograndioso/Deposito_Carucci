from membroSquadra import Membro

class Assistente(Membro):
    def __init__(self, nome: str, eta: int, specializzazione: str):
        
        super().__init__(nome, eta)
        
        self.specializzazione = specializzazione
        
    def supporta_team(self):
        print(f"L'assistente {self.nome}, specializzato in {self.specializzazione}, "
              f"sta supportando il team per la prossima partita.")
        
    