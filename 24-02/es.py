import numpy as np

def esegui_esercizio():
    nome_file = "risultati_esercizio.txt"
    
    scelta_mode = input("Vuoi sovrascrivere il file esistente (s) o aggiungere i dati in coda (a)? [s/a]: ").lower()
    mode = 'w' if scelta_mode == 's' else 'a'

    while True:
        array_lin = np.linspace(0, 10, 50)

        array_rand = np.random.random(50)

        nuovo_array = array_lin + array_rand

        somma_totale = np.sum(nuovo_array)

        somma_condizionata = np.sum(nuovo_array[nuovo_array > 5])

        print("-" * 30)
        print("Array Linspace (0-10):", array_lin)
        print("\nArray Random (0-1):", array_rand)
        print("\nNuovo Array (Somma):", nuovo_array)
        print(f"\nSomma Totale: {somma_totale}")
        print(f"Somma elementi > 5: {somma_condizionata}")
        print("-" * 30)

        with open(nome_file, mode) as f:
            f.write(f"--- Nuova Esecuzione ---\n")
            f.write(f"Somma Totale: {somma_totale}\n")
            f.write(f"Somma > 5: {somma_condizionata}\n")
            f.write(f"Array Risultante: {nuovo_array.tolist()}\n\n")
        
        mode = 'a'

        ancora = input("Vuoi eseguire un altro ciclo? (s/n): ").lower()
        if ancora != 's':
            print("Esecuzione terminata. I dati sono stati salvati in", nome_file)
            break

if __name__ == "__main__":
    esegui_esercizio()
