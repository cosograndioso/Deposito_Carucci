print("inserisci start o stop ")

risposta = input()
risposta.lower
match risposta:
    case "start":
        print("ciao")
    case "stop":
        print("sono fermo")
    case _:
        print("non valido")
        