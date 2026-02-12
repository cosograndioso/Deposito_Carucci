'''Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
Attributi privati:
_numero (intero): il numero del posto.
_fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).
Metodi:
__init__(numero, fila): inizializza il posto impostando _occupato a False.
prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
Classi Derivate
PostoVIP:
Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
Metodi:
Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.









PostoStandard:
Attributi aggiuntivi: costo  (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
Metodi:
Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
Classe Teatro
Attributi:
_posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
Metodi:
aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati.
'''



from posto import Posto
class Vip(Posto):
    def __init__(self, numero: str, fila: str, costo:int, extra: str):
        super().__init__(numero, fila)
        self.costo=costo
        self.extra=extra
    def get_extra(self):
        return f"Servizi inclusi: {self._extra}"
    
    
    def prenota(self):
        
       riuscito = super().prenota()
       if riuscito:
            print(f"--- ATTIVAZIONE SERVIZI VIP: {self._extra} ---")
        
       return riuscito








class PostoStandard(Posto):
    def __init__(self, numero, fila,  costo:int):
        super().__init__(numero, fila)
    
        self.costo= costo
    
    
    def prenota(self):
        
       riusc = super().prenota()
       if riusc:
            print(f"---  SERVIZI Standard ---") 
    