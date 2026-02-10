'''Esercizio 1 (Facile):
Crea una classe chiamata Punto. Questa classe dovrebbe avere:
Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.
'''

'''import math
class Punto:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
        
       
        
        
        
        def muovi(self, dx,dy):
           self.x= dx
           self.y= dy
          
        def distanza_da_origine(self):
            return math.sqrt(self.x**2 + self.y**2)
       
       
      
p1 = Punto(3, 4)
print(f"Posizione iniziale: ({p1.x}, {p1.y})")
print(f"Distanza iniziale: {p1.distanza_da_origine()}")

p1.muovi(2, 1) 
print(f"Nuova posizione: ({p1.x}, {p1.y})")       
            
'''

'''Esercizio 2 (Facile):
Crea una classe chiamata Libro. Questa classe dovrebbe avere:
Tre attributi: titolo, autore e pagine.
Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine."'''         
'''EXTRA: Andare a gestire nel primo esercizio X punti che sono X oggetti che deve definire tutti e stampare tutti assieme.'''
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
         
    def descrizione(self):
        return f"Libro: {self.titolo}, scritto da {self.autore}, pagine: {self.pagine}"

class Biblioteca:
    def __init__(self):
       
        self.lista_libri = []
        
    def aggiungi_libro(self, libro):
       
        self.lista_libri.append(libro)
        print(f"'{libro.titolo}' aggiunto alla bibliote")


mia_biblioteca = Biblioteca()

while True:
    print(" Inserimento Libro 'no' per uscire")
    titolo = input("Titolo: ")
    
    if titolo.lower() == 'no':
        break
        
    autore = input("Autore: ")
    
    pagine = int(input("Numero pagine: ")) 
    
   
    nuovo_libro = Libro(titolo, autore, pagine)
    
    
    
    
    mia_biblioteca.aggiungi_libro(nuovo_libro)


print("\nContenuto della biblioteca:")
for libro in mia_biblioteca.lista_libri:
    print(libro.descrizione())  
        
    
    
    
    
    
    
    
    
    
    
    
    
    



























            