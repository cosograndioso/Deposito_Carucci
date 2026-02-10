

class GestorePacchi:
    def __init__(self, magazzino):
        self.magazzino = magazzino

    def mettiInConsegna(self, pacco_id):
        self.magazzino.cambiaStatoPacco(pacco_id, "in consegna")

    def segnalaConsegnato(self, pacco_id):
        self.magazzino.cambiaStatoPacco(pacco_id, "consegnato")

    def pesoTotaleNonConsegnati(self):
        return sum(pacco.peso for pacco in self.magazzino.pacchi.values() if pacco.stato != "consegnato")
