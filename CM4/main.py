"""
@author: manuvai.rehua@ut-capitole.fr
"""

import requests
import json

def get_web_data(url: str) -> any:
    """Récupération des données sous forme d'un objet à partir de données JSON

    Args:
        url (str): L'url source

    Returns:
        any: Le contenu
    """
    response = requests.get(url)
    raw_data = response.text

    return json.loads(raw_data)

def search_by_name(name: str, data: list) -> dict:
    """Recherche à partir d'un nom de station

    Args:
        name (str): Le nom de la station à chercher
        data (list): La liste des stations

    Returns:
        dict: La station recherchée
    """
    for station in data:
        if (station['name'] == name):
            return station
    return None

def get_nb_bike_availables(data: list) -> int:
    """Récupération du nombre total de vélos disponibles

    Args:
        data (list): La liste des stations

    Returns:
        int: Le nombre de vélos disponibles
    """
    return get_sum_by_key(data, 'available_bikes')

def get_nb_bike_stands_availables(data: list) -> int:
    """Récupération du nombre total de places pour déposer un vélo disponibles

    Args:
        data (list): La liste des stations

    Returns:
        int: Le nombre de places pour déposer un vélo disponibles
    """
    return get_sum_by_key(data, 'available_bike_stands')

def get_nb_bike_stands(data: list) -> int:
    """Récupération du nombre total de places pour déposer un vélo

    Args:
        data (list): La liste des stations

    Returns:
        int: Le nombre de places pour déposer un vélo
    """
    return get_sum_by_key(data, 'bike_stands')

def get_sum_by_key(data: list, key: str) -> int:
    """Récupération de la somme d'une clé donnée

    Args:
        data (list): La liste des stations
        key (str): La clé donnée

    Returns:
        int: Le nombre total récupéré
    """
    count = 0

    for station in data:
        count += station[key]
    
    return count


if __name__ == '__main__':
    url = 'https://data.toulouse-metropole.fr/api/explore/v2.1/catalog/datasets/api-velo-toulouse-temps-reel/exports/json?lang=fr&timezone=Europe%2FParis'
    stations = get_web_data(url)

    # Question 1
    station_name = '00084 - BRIENNE - MANUFACTURE'
    station_searched = search_by_name(station_name, stations)

    if (station_searched is None):
        print("La station \"{}\" n'a pas pu être trouvée".format(station_name))
    else:
        print("Le nombre de vélos disponibles à la station '{}' est de {}".format(station_name, station_searched['available_bikes']))
        print("Le nombre de places disponibles à la station '{}' est de {}".format(station_name, station_searched['available_bike_stands']))

    # Question 2
    nb_bike_availables = get_nb_bike_availables(stations)
    nb_bike_stands_availables = get_nb_bike_stands_availables(stations)
    nb_bike_stands = get_nb_bike_stands(stations)
    
    print("Le nombre total de vélos disponibles actuellement (« Available Bikes ») est de : {}".format(nb_bike_availables))
    print(" Le nombre total de place disponibles pour déposer un vélo (Available Bike Stands) est de : {}".format(nb_bike_stands_availables))
    print("Le nombre total de « bike stands » est de : {}".format(nb_bike_stands))