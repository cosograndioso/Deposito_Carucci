conteggio = 0

while conteggio < 5:
    print(conteggio)
    
    conteggio +=1
    
    
controllore = True
while controllore:
    print("buonasera ")
e = input("vuoi uscire si o no?")


if (e.lower=="si"):
     controllore= False
else:
    controllore= True
     
     
n = [1,2,3]

for i in n :
    print(i)
    
    
while True:
    
    numero = int(input("Inserisci un numero: "))

   
    for i in range(numero, -1, -1):
        print(i)


    risposta = input("Vuoi ripetere? (s/n): ").lower()

    if risposta != "s":
        print("Programma terminato.")
        break

        
numeri_primi = []

while len(numeri_primi) < 5:
    numero = int(input("Inserisci un numero: "))

    if numero < 2:
        print("Il numero non è primo")
        continue

    primo = True

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("Il numero è primo")
        numeri_primi.append(numero)
    else:
        print("Il numero non è primo")

print("Hai inserito 5 numeri primi:", numeri_primi)

        

    