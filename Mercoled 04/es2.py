print("inserisci la tua eta per vederee il filom")

eta = int(input("Inserisci la tua età per vedere il film: "))

stato = "maggiorenne" if eta >= 18 else "minorenne"


match stato:
    case "maggiorenne":
        print("Puoi vedere il film")
    case "minorenne":
        print("Vai a casa pirla")
    case _:
        print("Errore")
        
        
        
#2
print("inserisci due numeri")
print("n1")
n1= int (input())

print("n2")
n2= int (input())

print("operazione +, -, *, /")

op = input()


match op:
    case "+":
        somma = n1+n2
        print("ecco la somma ", somma)
        
    case "-":
        sottr= n1-n2
        print("sottr", sottr)
        
    case "*":
        molt = n1*n2
        print("moltipl", molt)
    case "/":
        div = n1/n2
        print(div)
    case _:
        print("a coglione inserisci qualcosa")
        
        

#3
print("crea il tuo personaggio")
print("inserisci se sei m o f ")
risp = input()
risp.lower

match risp:
    case "m":
     print("insrisci la tua fazione Roma o lazio")
     ca= input()
     ca.lower
     match ca:
         case "roma":
             print("a maggica")
         case "lazio":
                 print("lotito merda")
    case "f":
       print("insrisci la tua fazione Roma o lazio")
       ca= input()
       ca.lower
       match ca:
         case "roma":
             print("a maggica")
         case "lazio":
                 print("lotito merda")
                 
    case _:
        print("forza juve")
       