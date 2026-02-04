


#3
print("scegli: crea, mostra")

scelta=input()
id_c=0
    


utenti=[]


if scelta.lower()=="crea":
    
    print("metti nome")
    nome =input()
    print("metti psw")
    pSW = input()
    id_c +=1
    
   
    utenti.append([id_c, nome, pSW ])  
    
    print(utenti)
else:
    print("zio can")  



print("vuoi continuare ad inserire un altro bastardo? si o no")
scelta2 = input()
    
if scelta2.lower()=="si":
 print("metti nome")
nome =input()

if nome.lower()  in utenti:
    print("nome non consentito")

else:

    print("metti psw")
pSW = input()
id_c +=1
    
   
utenti.append([id_c, nome, pSW ])  
    
print(utenti)



#1
x=1
y=2

if x==y:
    print("puoi passare")
elif x>y:
    print("puoi passare")
elif x>=y:
    print("puoi passare")
else: 
    print("vai fuori")
    
    

#2
lista = ["ciao"]

print("scrivi cosa vuoi fare: agg, del, exit")
scelta = input()

if scelta == "agg":
    elemento = input("Cosa vuoi aggiungere? ")
    lista.append(elemento)
    print(lista)

elif scelta == "del":
    elemento = input("Cosa vuoi eliminare? ")
    if elemento in lista:
        lista.remove(elemento)
    else:
        print("Elemento non trovato")
    print(lista)

elif scelta == "exit":
    print("Nessuna operazione")
    print(lista)

else:
    print("Input errato")








