<<<<<<< HEAD
class Automibile:
    n_ruote=4
    def __init__(self,marca,modello):
        self.marca= marca
        self.modello=modello
    def stampa_info(self):
        print("mobile", self.marca, self.modello)
    
    
    def __str__(self): #ci permette di stampare qualcosa quando viene chiamato il nome dell oggetto
        return("ciao")
        
auto1 = Automibile("fiat","ciao")
auto1.stampa_info()

#method static
class Calc:
    
    @staticmethod
    def somma(a,b):
        return a+b
risu = Calc.somma(5,3)
print(risu)

class Cont:
    n_ist=0
    
    def __init__(self):
        Cont.n_ist +=1
        
    @classmethod
    def mostra_ista(cls):
        print(f"ecco",cls.n_ist)
        

c1= Cont()
c2= Cont()

=======
class Automibile:
    n_ruote=4
    def __init__(self,marca,modello):
        self.marca= marca
        self.modello=modello
    def stampa_info(self):
        print("mobile", self.marca, self.modello)
    
    
    def __str__(self): #ci permette di stampare qualcosa quando viene chiamato il nome dell oggetto
        return("ciao")
        
auto1 = Automibile("fiat","ciao")
auto1.stampa_info()

#method static
class Calc:
    
    @staticmethod
    def somma(a,b):
        return a+b
risu = Calc.somma(5,3)
print(risu)

class Cont:
    n_ist=0
    
    def __init__(self):
        Cont.n_ist +=1
        
    @classmethod
    def mostra_ista(cls):
        print(f"ecco",cls.n_ist)
        

c1= Cont()
c2= Cont()

>>>>>>> 6f3b5d4de2cb9070e3d73296676c9aa6e7fe97d1
Cont.mostra_ista()