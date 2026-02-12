from abc import ABC, abstractmethod

class Animale (ABC):
    @abstractmethod
    def muovi():
        pass
    
class Cane (Animale):
    def muovi(self):
        pass
    
class Pesce (Animale):
    def muovi():
        pass