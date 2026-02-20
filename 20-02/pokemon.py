'''TRACCIA: Create un programma python utilizzando le api
https://pokeapi.co/api/v2/pokemon/ {numero} che simula un
pokedex, quando troverete un pokemon in maniera randomica
verificherà se è presente nel vostro pokedex (pokedex.json), in caso non fosse presente vi permetterà di catturarlo salvando le caratteristiche.
(Sul sistema API sono presenti poco più di 1000 pokemon)'''


import requests
import json
import random
import os
POKEDEX_FILE = "pokedex.json"

def ottieni_pokemon_random():
    """Recupera i dati di un Pokemon casuale dalle API."""
    pokemon_id = random.randint(1, 1025)  # Esistono circa 1025 Pokemon ad oggi
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Errore di connessione: {e}")
    return None


def ottieni_catch_rate(pokemon_id):
   
    url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    
    res = requests.get(url)
        
    return res.json()['capture_rate']
    







def Cattura(catch_rate):

    lancio = random.randint(1,225)
    print(f"lancio:  {lancio}")
    
    
    return lancio <= catch_rate


def MettiInSquadra(Pok_Catturato):
    nome_file = "/home/gabriele/Scrivania/Deposito_Carucci/20-02/pokedez.json"
    
    # 1. Carichiamo la lista esistente
    if os.path.exists(nome_file):
        with open(nome_file, "r") as file:
            try:
                lista = json.load(file)
            except:
                lista = []
    else:
        lista = [] # Se il file non esiste, partiamo da una lista vuota
    
    # 2. AGGIUNGIAMO il pokemon catturato alla lista (QUESTO MANCAVA!)
    lista.append(Pok_Catturato)
    
    # 3. Salviamo la lista aggiornata
    with open(nome_file, "w") as file:
        json.dump(lista, file, indent=4)
 
    return f"Ottimo lavoro! {Pok_Catturato['nome']} è ora nel file JSON."
   
   
   
   
   


RISS = ottieni_pokemon_random()

if RISS:
    
    nome = RISS['name'].upper()
    identificativo = RISS['id']
    altezza = RISS['height']
    peso = RISS['weight']
    
    tipi = ", ".join([t['type']['name'] for t in RISS['types']])

    print("-" * 30)
    print(f"POKEMON TROVATO!")
    print(f"Nome:    {nome}")
    print(f"ID:      #{identificativo}")
    print(f"Tipo/i:  {tipi}")
    print(f"Altezza: {altezza}")
    print(f"Peso:    {peso}")
    cattura = ottieni_catch_rate(identificativo)
    print(f"cath rate",cattura)
    print("-" * 30)
    
    
    while(True):
     
     risp= input("vuoi tentare una cattura s o n:   ").lower()
     
     if risp =="s":
        
        if Cattura(cattura):
            print("Cattura completata!")
            
            # Creiamo il dizionario con i dati reali del pokemon
            dati_per_pokedex = {
                "id": identificativo,
                "nome": nome,
                "tipo": tipi,
                "peso": peso
            }
            
            # Passiamo i dati alla funzione
            risultato_salvataggio = MettiInSquadra(dati_per_pokedex)
            print(risultato_salvataggio)
            break
        

     else:
        print("uscita")
        break
   
   



