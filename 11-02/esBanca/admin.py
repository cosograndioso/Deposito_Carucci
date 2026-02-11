
from utenti import Utente
class Admin(Utente):
    
    def __init__(self, nome: str, cognome: str, id_admin: str):
        
        database_admin = {
        "boss_admin": {"psw": "admin2024", "oggetto": Admin("Sofia", "Bianchi", "ADM-001")}
        }
        
        
        
        super.__init__(nome,cognome)
        
        
        
        self.__id_admin = id_admin
       
    def get_id_admin(self):
     return self.__id_admin
 
 
    def vedi_conto(self, id_utente, database_conti):
        
        if id_utente in database_conti:
            conto = database_conti[id_utente]
            print(f"--- ISPEZIONE ADMIN ---")
            
            conto.visualizzaSaldo() 
        else:
            print(f"Errore: Nessun conto associato all'utente '{id_utente}'")
       
    
    
       
       
       
       
       
       
       
       
       
     
        
        
