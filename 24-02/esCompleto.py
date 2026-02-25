import numpy as np

def salva_su_file(operazione, dati):
    with open("risultati_matrice.txt", "a") as f:
        f.write(f"--- {operazione} ---\n")
        f.write(str(dati) + "\n\n")

def sistema_matrici():
    matrice = None
    
    while True:
        print("\n--- MENU GESTIONE MATRICE ---")
        print("1. Crea nuova matrice (dimensioni utente)")
        print("2. Estrai sotto-matrice centrale")
        print("3. Trasponi matrice e stampa")
        print("4. Calcola somma totale")
        print("5. Esegui Esercizio 2(Fancy Indexing 4x4)")
        print("6. Esci")
        
        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            r = int(input("Righe: "))
            c = int(input("Colonne: "))
            matrice = np.random.randint(1, 101, (r, c))
            print("Matrice:\n", matrice)
            salva_su_file("Nuova Matrice", matrice)

        elif scelta == "2":
            if matrice is not None and matrice.shape[0] > 2 and matrice.shape[1] > 2:
                sotto_matrice = matrice[1:-1, 1:-1]
                print("Sotto-matrice centrale:\n", sotto_matrice)
                salva_su_file("Sotto-matrice centrale", sotto_matrice)
            else:
                print("Matrice non esistente o troppo piccola per estrarre il centro.")

        elif scelta == "3":
            if matrice is not None:
                trasposta = matrice.T
                print("Trasposta:\n", trasposta)
                salva_su_file("Matrice Trasposta", trasposta)
            else:
                print("Crea prima una matrice!")

        elif scelta == "4":
            if matrice is not None:
                somma = np.sum(matrice)
                print(f"Somma: {somma}")
                salva_su_file("Somma Elementi", somma)
            else:
                print("Crea prima una matrice!")

        elif scelta == "5":
            # Logica specifica dell'Esercizio 3
            ex3_arr = np.random.randint(10, 51, (4, 4))
            print("Array 4x4 (10-50):\n", ex3_arr)
            
            r_idx, c_idx = [0, 1, 2, 3], [1, 3, 2, 0]
            sel = ex3_arr[r_idx, c_idx]
            print("Elementi (0,1), (1,3), (2,2), (3,0):", sel)
            
            dispari = ex3_arr[[1, 3]]
            print("Righe dispari (1 e 3):\n", dispari)
            
            ex3_arr[r_idx, c_idx] += 10
            print("Array dopo +10 ai selezionati:\n", ex3_arr)
            
            salva_su_file("Esercizio Fancy Indexing", ex3_arr)

        elif scelta == "6":
            break
        else:
            print("Scelta non valida.")

if __name__ == "__main__":
    sistema_matrici()