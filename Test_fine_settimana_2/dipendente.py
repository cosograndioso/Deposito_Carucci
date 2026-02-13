
from abc import ABC, abstractmethod

class Dipendente(ABC):
    def __init__(self, nome:str , cognome:str , id_badge:int):
        self.__nome= nome
        self.__cognome= cognome #incaspulamento 
        self.__id_badge=id_badge
    
    
    def Get_nome(self): #per vedere in modo sicuro i dati incaspulati
        return self.__nome
    
    
    def Set_nome(self, nuovo_nome): #per settari i dati incaspulati
        if len(nuovo_nome) > 0:
            self.__nome = nuovo_nome  
        else:
            print("Errore: Il nome non può essere vuoto.")
            
            
    
    def Get_cognome(self):
        return self.__cognome
    
    def Set_cognome(self, nuovo_cognome):
        self.__cognome = nuovo_cognome
        
    def Get_id_badge(self):
        return self.__id_badge    
    
    
    
    def id_badge(self, nuovo_id):
        
        if nuovo_id > 0:
            self.__id_badge = nuovo_id
        else:
            print("Errore: ID Badge non valido.")
            
    # METODO ASTRATTO: non ha corpo, è un "obbligo" per i figli
    @abstractmethod
    def calcola_privilegi(self):
        """Ogni tipo di dipendente deve definire i propri privilegi"""
        pass
            
    def info(self):
        return f"Dipendente: {self.Get_nome()} {self.Get_cognome()} | Badge: {self.Get_id_badge()}"