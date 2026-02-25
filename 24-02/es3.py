import numpy as np

array = np.random.randint(10, 51, (4, 4))
print("Array originale:\n", array)

righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]
elementi_selezionati = array[righe, colonne]
print("\nElementi selezionati:", elementi_selezionati)

righe_dispari = array[[1, 3]]
print("\nRighe dispari (1 e 3):\n", righe_dispari)

array[righe, colonne] += 10
print("\nArray modificato:\n", array)