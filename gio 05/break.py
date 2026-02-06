n = [1,2,3,5]

for n in n :
    if n==3:
        break #chiude
    
    
n = [1,2,3,5]

for n in n :
    if n==3:
        continue#per eclusioni
    print(n)
    
for n in n :
    if n==3:
        pass#a nulla
    print(n)
    
    
    
num= [*range (1,11)] #splat

print(num) #L’asterisco * è l’operatore di unpacking. Serve per “spacchettare” i valori del range dentro una lista.