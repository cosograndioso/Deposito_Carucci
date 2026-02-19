
stringa = input("Inserisci una stringa: ")


frequenza = {}


for carattere in stringa:
    if carattere in frequenza:
        
        frequenza[carattere] += 1
    else:
        
        frequenza[carattere] = 1


print("Frequenza dei caratteri:")
print(frequenza)