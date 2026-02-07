
#generatore
def fibonacci (n):
    a,b =0, 1
    while a < n :
        yield a 
        a,b=b, a + b


for numero in fibonacci(20):
    print(numero)
    

print(*fibonacci(20))
        
        
def contafinoN(n):
    i=1
    while i<=n:
        yield i
        i+=1

for numero in contafinoN(20):
    print(numero)
    
    
def catenaGen ():
    yield from range(1,4)

    yield from range(10,13)



print(list(catenaGen()))


#decoratore
def decoratore (funzione):
    def wrapper():
        print("prima")
        funzione()
        print("dopo")
    return wrapper

@decoratore
def saluta():
    print("ciao")
    
saluta()



#wrapper
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b


print( "la somam e ",somma(3, 4))



def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Chiamata alla funzione decorata
print(moltiplica(3, 4))