import requests

def ottieni_coordinate(citta):
    """
    Riceve il nome di una città e restituisce una tupla (latitudine, longitudine).
    In caso di errore o città non trovata, restituisce (None, None).
    """
  
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={citta}&count=1&language=it&format=json"
   
    
    
    
    
    
    
    
    try:
        response = requests.get(url)
        
        data = response.json()
        
        
        if "results" in data and len(data["results"]) > 0:
            lat = data["results"][0]["latitude"]
            lon = data["results"][0]["longitude"]
            return lat, lon
        else:
            print(f"Città '{citta}' non trovata.")
            return None, None
            
    except Exception as e:
        print(f"Errore durante la ricerca: {e}")
        return None, None


nome_citta = input("Inserisci il nome della città: ")
lat, lon = ottieni_coordinate(nome_citta)

if lat and lon:
    print(f"Coordinate di {nome_citta}:")
    print(f"Latitudine: {lat}")
    print(f"Longitudine: {lon}")
    
    
    
    
    

    




