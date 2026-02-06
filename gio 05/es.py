#1

scelta = input("s o n?: ")
scelta =scelta.lower()

match scelta:
    case "s":
        print("hai scelto stringa")
    case "n": 
        print("hai scelto numero")
        n = int (input("inserisci il numero"))
        if n%2==0:
            print("il tuo nu7mero e pari", n)
        else:
            print(f"{n} è dispari")
            
            
'''2.Intermedio/ Numeri primi in un intervallo :
Chiedi all'utente di inserire due numeri che definiscono un intervallo (es 10 e 50).
Il programma dovrebbe stampare tutti i numeri primi compresi in 
quell'intervallo o i numeri non primi o entrambi divisi a tua scelta,
salvandoli in due aggregazioni differenti e chiedere se deve ripetere '''


while True:

    n1 = int(input("n1? "))
    n2 = int(input("n2? "))

    if n1 > n2:
        n1, n2 = n2, n1

    primi = []
    non_primi = []

    for i in range(n1, n2 + 1):

        if i < 2:
            non_primi.append(i)
            continue

        primo = True
        #Serve per controllare se il numero i ha divisori quindi per capire se è primo.
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                primo = False
                break

        if primo:
            primi.append(i)
        else:
            non_primi.append(i)

    print("Numeri primi:", primi)
    print("Numeri NON primi:", non_primi)

    r = input("Vuoi ripetere bastardo? (s/n): ").lower()

    if r != "s":
        break



'''.Avanzato/ Fattori comuni Descrizione:
Chiedi all'utente di inserire due numeri. Il programma dovrebbe determinare e stampare i fattori comuni di entrambi i numeri. Se non ci sono fattori comuni oltre 1, dovrebbe stampare "I numeri sono coprimi".
La stessa cosa ma anche per due stringhe (.equal ) e chiedere se deve ripetere ma sono “ complementari” solo se hanno tutte le lettere in comune (es:abs/ sab) 
    
n1 = int(input("n1? "))
n2 = int(input("n2? "))

fattori_comuni = []
for i in range(n1, n2 + 1):
'''