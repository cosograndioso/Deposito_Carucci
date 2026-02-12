'''creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.'''



class MetodoDiPagamento:
    
    def __init__(self, importo):

            self.importo=importo
      
        
        
class CartaDiCredito(MetodoDiPagamento):
    def effettua_pagamento(self, importo):
        return f"Pagamento di {importo}€ effettuato con Carta di Credito (Transazione sicura)."

class PayPal(MetodoDiPagamento):
    def effettua_pagamento(self, importo):
        return f"Pagamento di {importo}€ effettuato tramite PayPal (Email inviata)."

class BonificoBancario(MetodoDiPagamento):
    def effettua_pagamento(self, importo):
        return f"Pagamento di {importo}€ effettuato via Bonifico (In attesa di conferma)."
    
    
class GestorePagamenti:
    def __init__(self, metodo: MetodoDiPagamento):
        self.metodo = metodo
        
    def processa(self, cifra):
        
        risultato = self.metodo.effettua_pagamento(cifra)
        print(risultato)
        







