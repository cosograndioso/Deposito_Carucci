registro = {}

while True:
    nome = input("Inserisci il nome dell'alunno (o scrivi 'media' per terminare): ")
    
   
    if nome.lower() == "media":
        break
    
    
    if nome not in registro:
        registro[nome] = []
    
  
    while True:
        voto_input = input(f"Inserisci un voto per {nome} (o scrivi 'stop' per passare al prossimo alunno): ")
        
        if voto_input.lower() == "stop":
            break
        
        
        voto = float(voto_input)
        registro[nome].append(voto)


print(" RISULTATI ")

for nome, voti in registro.items():
    if len(voti) > 0:
        media = sum(voti) / len(voti)
        print(f"Nome: {nome}, Media: {media}")
    else:
        print(f"Nome: {nome}, Media: Nessun voto inserito")