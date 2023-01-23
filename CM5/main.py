import json
import requests
import matplotlib.pyplot as plt

def get_data(url: str) -> dict:
    """Permet la récupération des données

    Args:
        url (str): L'URL vers les données source

    Returns:
        dict: Les données de retour
    """
    r = requests.get(url)

    json_data = json.loads(r.text)

    return json_data

def get_years_interval(start: int, end: int) -> list:
    """Génération de l'intervalle entre deux années incluses

    Args:
        start (int): L'année de départ
        end (int): L'année de fin

    Returns:
        list: L'intervalle
    """
    response = []
    for i in range(start, end + 1):
        response.append(i)

    return response

def get_temperatures(country_data: dict, years_interval: list) -> list:
    """Récupération des températures d'un pays selon un intervalle donné

    Args:
        country_data (dict): Les données du pays
        years_interval (list): L'intervalle d'années

    Returns:
        list: La liste des températures
    """
    response = []

    for year in years_interval:
        year_temperature = country_data["properties"]["F" + str(year)]
        response.append(year_temperature)
    
    return response

def find_by_country(country_name: str, data: dict) -> dict:
    """Implémentation de la recherche des données d'un pays donné

    Args:
        country_name (str): Le nom d'un pays à trouver
        data (dict): La liste des données

    Returns:
        dict: Le pays cherché
    """
    for country_data in data['features']:
        if (country_data["properties"]["Country"] == country_name):
            return country_data

def add_curve(ax: plt.Axes, x_data: list, y_data: list, label: str):
    """Ajout d'une courbe à un axe

    Args:
        ax (plt.Axes): L'objet permettant le dessin
        x_data (list): Les données en abscisses
        y_data (list): Les données en ordonnées
        label (str): Le label à donner à la courbe
    """
    ax.plot(x_data, y_data, label=label)

def add_country_curve(ax: plt.Axes, country_name: str, years_interval: list, data: dict):
    """Simplification de l'appel à la méthode add_curve avec des données préparées

    Args:
        ax (plt.Axes): L'objet permettant le dessin
        country_name (str): Le nom d'un pays
        years_interval (list): L'intervalle d'années
        data (dict): Les données sources
    """
    country_data = find_by_country(country_name, data)
    country_temperatures = get_temperatures(country_data, years_interval)
    add_curve(ax, years_interval, country_temperatures, country_name)


if __name__ == '__main__':
    url = "https://services9.arcgis.com/weJ1QsnbMYJlCHdG/arcgis/rest/services/Indicator_3_1_Climate_Indicators_Annual_Mean_Global_Surface_Temperature/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"
    data = get_data(url)

    start_year = 1961
    end_year = 2021
    years_interval = get_years_interval(start_year, end_year)

    fig, ax = plt.subplots()
    countries_names = ["France", "Australia", "Iceland", "Spain", "Philippines", "World"]

    # Partie 1 et 2
    for country_name in countries_names:
        add_country_curve(ax, country_name, years_interval, data)

    ax.set_xlabel("Années")
    ax.set_ylabel("Températures")
    ax.set_title("Évolution des températures selon les pays") 
    ax.legend()
    plt.show()

    # Partie 3
    temperatures = []
    year_concerned = 2021

    for country_name in countries_names:
        country_data = find_by_country(country_name, data)
        year_temperature = country_data["properties"]["F" + str(year_concerned)]
        temperatures.append(year_temperature)

    fig, ax = plt.subplots() 
    ax.bar(countries_names, temperatures);  
    ax.set_title("Évolution des températures selon les pays en 2021") 

    plt.show()   

