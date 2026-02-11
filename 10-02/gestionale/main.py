from elettronica import Elettronica

from fabbrica import Fabbrica

def menu():
    print("\n--- GESTIONALE FABBRICA (Solo Elettronica) ---")
    print("1. Aggiungi Laptop all'inventario")
    print("2. Vendi Laptop")
    print("3. Reso Laptop")
    print("4. Mostra Inventario")
    print("0. Esci")
    return input("Scegli un'opzione: ")


pc = Elettronica("Laptop", 800, 1200, 24)


mia_fabbrica = Fabbrica()


mentre_attivo = True

while mentre_attivo:
    scelta = menu()

    if scelta == "1":
        qta = int(input("Quanti Laptop vuoi aggiungere? "))
        mia_fabbrica.aggiungi_prodotto(pc, qta)

    elif scelta == "2":
        qta = int(input("Quanti Laptop vuoi vendere? "))
        mia_fabbrica.vendi_prodotto(pc, qta)

    elif scelta == "3":
        qta = int(input("Quanti Laptop sono stati resi? "))
        mia_fabbrica.resi_prodotto(pc, qta)

    elif scelta == "4":
        print("\n--- STATO INVENTARIO ---")
       
        if not mia_fabbrica.inventario:
            print("Il magazzino è vuoto.")
        else:
            for prod, qta in mia_fabbrica.inventario.items():
                print(f"{prod.nome}: {qta} unità in magazzino")

    elif scelta == "0":
        print("Chiusura gestionale. Arrivederci!")
        mentre_attivo = False
    
    else:
        print("Opzione non valida, riprova.")