"""Fonctions pour la manipulation de texte"""

def formate_nom(nom : str) -> str:
    """Fonction qui formate le nom entré et retourne 
        un nom de la forme 'mon-nom-d-anime"""

    new_name = nom.lower().strip()  # Transforme l'entrée en lettres minuscules puis enlève les espaces autour du mot
    new_name = new_name.replace(" ", "-")

    return new_name


def new_url(url : str, nom_video : str) -> str:
    """Fonction qui retourne l'url spécifique
       à un contenu en partant d'une url de base """
    
    nom = formate_nom(nom_video)

    return url + nom


