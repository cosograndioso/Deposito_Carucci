while True:
    parDisp = int(input("Inserisci un numero: "))

  
    if parDisp % 2 == 0:
        print("Pari")
    else:
        print("Dispari")

    
    if parDisp >= 0:
       
        for nu in range(parDisp, -1, -1):
            print(nu)
    else:
        print("Il numero non è positivo, non posso scalare a 0.")
    
   
    break
    
    
count=0
max=0
lista = [2,2,3]

for i in lista:
    quadrat = i*i
    print(quadrat)  

 
 #MASS
for i in lista:
    
    if i>max:
        max=i
    print("munero massimo nella lista", max)
    

#n numeri presenti nella lista 


if len(lista) == 0:
    print("Lista Vuota")
else:
    
    massimo = lista[0]
    for numero in lista:
        if numero > massimo:
            massimo = numero

    
    conteggio = 0
    indice = 0
    while indice < len(lista):
        conteggio = conteggio + 1
        indice = indice + 1

    
    print("Numero massimo trovato:", massimo)
    print("Numero di elementi nella lista:", conteggio)


 
    
    
    