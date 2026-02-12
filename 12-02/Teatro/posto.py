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



class Posto:
    def __init__(self, numero:str, fila:str):
       self._numero=numero
       self._fila=fila
       self._occupato=False
       
    def is_occupato(self):
        return self._occupato
    
    
    def prenota(self):
        
       if not  self._occupato:
           self._occupato=True
           print(f"Posto {self._fila}{self._numero} prenotato con successo!")   
           return True
       
       else:
           print(f"Spiacente, il posto {self._fila}{self._numero} è già occupato.")
           return False
       
    def libera(self):
        
     if self._occupato:
        self._occupato=False
        return f"Posto {self._fila}{self._numero} liberato con successo!"
     else:
       return f"Posto {self._fila}{self._numero} era gia' libero!"  
    