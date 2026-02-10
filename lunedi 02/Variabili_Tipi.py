

#stringa  e stampa
ciao = ("ciao mondo")
c =5
print("out ", c, ciao)

#input e conversione in intero

y= int (input("inserisci un valore y: "))

x = int(input("inserisci un numero x: "))
print("hai inserito ", x)

print ("cosa hai inserito " ,y, x )

#somma in print
print("somma casuale", 3+2)
#elevamento a potenza
print(2**2)


#somma e sottrazione con variabili
risultato2 = x-y
print("risultato2 ", risultato2)
risultato = x+y
print("risultato ", risultato)



#def stringhe
mirko = "mirko"
paolo = "paolo"


#concanetazione
print(mirko + " e " + paolo)

#singolo 

''' o doppio apice
print('mirko e paolo')

print("mirko e paolo")

print('mirko e "paolo"')

'''


fratm_gigi = "gigi"



v = 5       #int
print (v)
 
 
f=3.2 #float

print (f)

#chiedo unan stringa in input
lettera = input("inserisci una lettera: ")
#prima lettera della stringa
print(lettera[0])


saluto = "ciao"
nome = "gab"
saluto_completo = saluto + "come stai " + nome
print(saluto_completo)

#lunghezza della stringa
print(len(saluto_completo))  

#tutto maiuscolo
print(saluto_completo.upper())  
#tutto minuscolo 
print(saluto_completo.lower())     
#sostituisco a con o
print(saluto_completo.replace("a", "o")) 
print(saluto_completo.split(" "))  #divido la stringa in corrispondenza degli spazi
print(saluto_completo.split(" , "))  #divido la stringa in corrispondenza deglle virgole


#char
k = 'c'


#boolean
booleT =  True
boolef = False 

stampa = print  ( booleT, boolef)


x = 1 
y=1 

print(x==y) # confronto se e' uguale 
print(x!=y) #negazione 
print(x<y)  #se x e' minore true o false
