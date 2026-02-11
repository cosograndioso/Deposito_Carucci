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



class Conto:
    
    def __init__(self, titolare:str, saldo:float):
        self.set_titolare(titolare)
        self.__saldo = saldo if saldo >= 0 else 0

    
    
    
    
    
    
    
    
    
    def get_titolare(self):
        return self.__titolare
    
    
   # IL SETTER: Qui mettiamo i controlli che avevi copiato
    def set_titolare(self, valore: str):
        if isinstance(valore, str) and valore.strip():
            self.__titolare = valore
        else:
            # Valore di default in caso di errore
            self.__titolare = "Sconosciuto"
            print("Errore: Il titolare deve essere una stringa non vuota.")
    
    
    
    
    
    
    def visualizza_saldo(self):
        return self.__saldo
    
    
    
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print(f"hai depositato {importo}$")
        else: 
            print("importo non valido")
            
        
    
    def preleva(self, importo): 
        if importo>0:
            
            if self.__saldo >= importo:
                self.__saldo-= importo
                print(f" hai prelevato {importo}$")
            else:
                print("saldo non sufficente")
        else:
            print("deve essre positivo ")
    
    def visualizzaSaldo(self):
            print(f"saldo attuale di {self.__titolare}, ammonta a {self.__saldo}$")
            return self.__saldo