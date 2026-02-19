






def check_palindroma(testo):
    
    testo_pulito = testo.replace(" ", "").lower()
    
    # 2 Inversione: creiamo la versione al contrario della stringa
    testo_invertito = testo_pulito[::-1]
    
    # 3 Confronto: restituisce True se sono uguali, False altrimenti
    return testo_pulito == testo_invertito


frase = input("Inserisci una parola o una frase: ")

if check_palindroma(frase):
    print(f"'{frase}' è palindroma!")
else:
    print(f"'{frase}' non è palindroma.")