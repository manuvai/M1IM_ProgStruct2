"""
@author: manuvai-rehua@ut-capitole.fr
"""

import os

def get_data(csv_file_path: str) -> dict:
    """Implémentation de la récupération des films

    Args:
        csv_file_path (str): Le chemin vers le fichier CSV

    Returns:
        list: La liste des films
    """
    lines = get_file_lines(csv_file_path)
    
    keys = get_csv_keys(lines)

    liste_films = {}
    for i in range(1, len(lines)):
        data_dict = create_dict(lines[i], keys)
        film = create_film(data_dict)
        liste_films.update(film)

    return liste_films

def get_csv_keys(lines: list) -> list:
    """Permet de récupérer la liste des champs

    Args:
        lines (list): Les lignes du fichier CSV

    Returns:
        list: La liste des champs
    """
    return lines[0].split(';')

def get_file_lines(csv_file_path: str) -> list:
    """Implémentation de la récupération des lignes d'un fichier sans \n

    Args:
        csv_file_path (str): Le chemin vers le fichier CSV

    Returns:
        list: La liste des lignes
    """
    
    with open(csv_file_path) as file:
        lines = file.readlines()
    
    response = []

    for line in lines:
        response.append(line.replace("\n", ""))

    return response

def film_par_annee(annee: int, data: dict):
    """Implémentation du tri des films ayant été parus la même année et écriture dans un fichier

    Args:
        annee (int): Année donnée
        data (dict): Liste des films
    """
    films_filtres = {}

    for titre, data_film in data.items():
        if (data_film['Year'] == str(annee)):
            films_filtres[titre] = data_film
    filename = 'film-{}.csv'.format(str(annee))
    write_films_csv(films_filtres, filename)

def meilleurs_films(films: dict) -> dict:
    """Récupération des films ayant recu la meilleure popularité

    Args:
        films (list): La liste des films

    Returns:
        list: La liste des meilleurs films
    """
    best_film = meilleur_film(films)
    best_film_dict = film_to_dict(best_film)

    best_index = list(best_film.keys())[0]
    best_films = {}
    best_films[best_index] = best_film
    for titre, donnees_film in films.items():
        film_dict = film_to_dict({
            titre: donnees_film
        })

        film_pop = 0
        
        if (len(film_dict['Popularity']) > 0):
            film_pop = int(film_dict['Popularity'])
        
        best_film_pop = 0
        
        if (len(best_film_dict['Popularity']) > 0):
            best_film_pop = int(best_film_dict['Popularity'])

        bol_popu_egale = film_pop == best_film_pop
        bol_meme_film = best_film_dict['Title'] == film_dict['Title']

        if (bol_popu_egale and not bol_meme_film):
            best_films.update({
            titre: donnees_film
        })
    
    return best_films
    
def meilleur_film(films: dict) -> dict:
    """Récupération du film ayant reçu le plus de popu

    Args:
        films (list): La liste des films

    Returns:
        dict: Le meilleur film
    """
    best_index = list(films.keys())[0]
    best_film = film_to_dict({
            best_index: films[best_index],
        })

    for titre, data_film in films.items():
        film = film_to_dict({
            titre: data_film,
        })
        film_pop = 0
        
        if (len(film['Popularity']) > 0):
            film_pop = int(film['Popularity'])
        
        best_film_pop = 0
        
        if (len(best_film['Popularity']) > 0):
            best_film_pop = int(best_film['Popularity'])

        if (film_pop > best_film_pop):
            best_index = titre
            best_film = film_to_dict({
            best_index: films[best_index],
        })

    return {
        best_index: films[best_index],
    }

def films_awarded(films: list) -> list:
    """Récupération de la liste des films ayant recu un prix

    Args:
        films (list): La liste des films

    Returns:
        list: La liste des films ayant recu un prix
    """
    films_filtres = []

    for film in films:
        for titre, data_film in film.items():
            if (data_film['Awards'] == 'Yes'):
                films_filtres.append(film)
    return films_filtres
    
def meilleurs_films_awarded(films: list) -> dict:
    """Récupération de la liste des meilleurs films ayant recu un prix

    Args:
        films (list): La liste des films

    Returns:
        list: La liste des meilleurs films ayant recu un prix
    """

    films = films_awarded(films)

    best_films_awarded = meilleurs_films(films)

    return best_films_awarded

def film_to_dict(film: dict) -> dict:
    """Conversion vers un format dictionnaire plus gérable

    Args:
        film (dict): Film 

    Returns:
        dict: Film
    """
    response = {}
    for titre, data in film.items():
        response['Title'] = titre

        for key, value in data.items():
            response[key] = value
    return response

def film_to_line(film: dict) -> str:
    """Conversion vers une chaîne de caractère pour être insérée dans un fichier CSV

    Args:
        film (dict): Film

    Returns:
        str: La ligne correspondant à un film
    """
    film_dico = film_to_dict(film)

    temp_list = []
    temp_list.append(film_dico['Year'])
    temp_list.append(film_dico['Length'])
    temp_list.append(film_dico['Title'])
    temp_list.append(film_dico['Subject'])
    temp_list.append(film_dico['Main Actress'])
    temp_list.append(film_dico['Main Actor'])
    temp_list.append(film_dico['Director'])
    temp_list.append(film_dico['Popularity'])
    temp_list.append(film_dico['Awards'])

    return ";".join(temp_list)

def write_films_csv(films: dict, filename: str):
    """Implémentation de l'écriture d'une liste de films dans un fichier

    Args:
        films (dict): Liste des films
        filename (str): Nom du fichier
    """
    with open(filename, mode='w+') as file:
        file.write("Year;Length;Title;Subject;Main Actor;Main Actress;Director;Popularity;Awards")

    for titre, data_film in films.items():

        film = {
            titre: data_film
        }
        line = film_to_line(film)

        with open(filename, mode='a+') as file:
            file.write("\n" + line)


def create_film(data_dict: dict) -> dict:
    """Conversion vers un format démandé

    Args:
        data_dict (dict): Film

    Returns:
        dict: Film
    """
    return {
        data_dict['Title']: {
            'Year': data_dict['Year'],
            'Length': data_dict['Length'],
            'Subject': data_dict['Subject'],
            'Main Actress': data_dict['Main Actress'],
            'Main Actor': data_dict['Main Actor'],
            'Director': data_dict['Director'],
            'Popularity': data_dict['Popularity'],
            'Awards': data_dict['Awards'],
        }
    }

def pourcentage_meilleurs_films_avec_award(films: list) -> float:
    """Récupération du pourcentage de meilleurs films par rapport aux films ayant recu un prix

    Args:
        films (list): Liste de films

    Returns:
        float: Pourcentage (0 <= x <= 1)
    """
    bests = meilleurs_films(films)
    bests_awarded = meilleurs_films_awarded(films)
    nb_bests = len(bests)
    nb_bests_awarded = len(bests_awarded)

    return nb_bests_awarded / nb_bests

def create_dict(line: str, keys: list) -> dict:
    """Conversion d'une ligne vers un format exploitable de Film

    Args:
        line (str): La ligne
        keys (list): La liste de clés

    Returns:
        dict: Film
    """
    donnees = line.split(';')

    data = {}

    for i in range(len(donnees)):
        data[keys[i]] = donnees[i]

    return data

if (__name__ == '__main__'):
    films = get_data('./film.csv')
    print(films)
    print(film_par_annee(1990, films))
    print(meilleur_film(films))
    print(meilleurs_films(films))
    # print(films_awarded(films))
    # print(meilleurs_films_awarded(films))
    # print("Le pourcentage de meilleurs films ayant reçu un prix est de {} %".format(pourcentage_meilleurs_films_avec_award(films) * 100))
    

