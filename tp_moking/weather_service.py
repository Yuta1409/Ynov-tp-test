import requests, json
from requests.exceptions import RequestException
from datetime import datetime

def get_temperature(city):
    """Récupère la température d'une ville via une API"""
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city, # Nom de la ville
        'appid': '441f54eb9b8819b3a05d1674294bb055',  # Remplacez par votre clé API OpenWeather
        'units': 'metric'  # Pour obtenir la température en Celsius
    }
    
    # Effectue la requête à l'API
    # Utilise un bloc try-except pour gérer les exceptions potentielles
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            return temperature
        else:
            return None
    except RequestException:
        return None
    
def save_weather_report(city,filename='weather_log.json'):
    #Recupère la température
    temp = get_temperature(city)
    if temp is None:
        return False

    #Créer un rapport
    report = {
        'city': city,
        'temperature': temp,
        'date': datetime.now().isoformat()
    }
    
    #Sauvegarde le rapport
    try:
        with open(filename, 'r') as f:
            reports = json.load(f)
    except FileNotFoundError:
        reports = []
    reports.append(report)
    with open(filename, 'w') as f:
        json.dump(reports, f)
        
    return True
        