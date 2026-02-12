
from metodoPagamento import MetodoDiPagamento
from metodoPagamento import CartaDiCredito
from metodoPagamento import PayPal
from metodoPagamento import BonificoBancario
from metodoPagamento import GestorePagamenti



    
print("--- BENVENUTO ALLA CASSA ---")
totale_da_pagare = 150.0
while True:
        print(f"\nTotale ordine: {totale_da_pagare}€")
        print("Scegli il metodo di pagamento:")
        print("1. Carta di Credito")
        print("2. PayPal")
        print("3. Bonifico Bancario")
        print("4. Annulla e Esci")
        
        scelta = input("Seleziona un'opzione (1-4): ")
        

        # 1. Selezione dell'istanza (Polimorfismo)
        if scelta == "1":
            
            
            metodo_scelto = CartaDiCredito(totale_da_pagare)
        elif scelta == "2":
            metodo_scelto = PayPal(totale_da_pagare)
        elif scelta == "3":
            metodo_scelto = BonificoBancario(totale_da_pagare)
        elif scelta == "4":
            print("Operazione annullata.")
            break
        else:
            print("Opzione non valida, riprova.")
            continue

        # 2. Uso del GestorePagamenti
        # Il gestore riceve l'oggetto specifico (PayPal, Carta o Bonifico)
        gestore = GestorePagamenti(metodo_scelto)
        
        print("\nElaborazione in corso...")
        gestore.processa(totale_da_pagare)
        
        # Una volta pagato, usciamo dal ciclo
        print("Grazie per il tuo acquisto!")
        break
    
    
    
    
    
    
   