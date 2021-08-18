import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_video_links(url):
    # Create response object 
    print("Requête envoyée ...")
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, "html5lib")

    # Cherche tous les liens sur la page
    print("Récupération des liens ...")
    liens = soup.findAll('a') # Cherche toutes les balises <a>, celles qui comportent les liens
    # Liste avec les liens 
    
    liste_lien = [str(lien) for lien in liens]
    tous_liens = [ref for ref in liste_lien if "src" in ref]
    
    vrai_liens = [video for video in tous_liens]

    return vrai_liens 


def tri_balise(liste_parent : list, startswith : str, separateur : str = " " ) -> list:
    """ Fonction qui tri les éléments d'une liste comportants de nombreuses balises HTML
        et renvoie une liste contenant exclusivement la balise choisie.
        ---------------------------------------------------------------
        Arguments:
            - liste_parents : list 
                Liste dans laquelle on effectue le tri
            - startwith : str
                Première lettres de la balise souhaitée. Ex : "https", "src", "href" ...
            - separateur : str
                Élément à partir duquel on coupe chaque ligne de la liste parent."""
        
    new_list = list()
    for i in tqdm(range(len(liste_parent))):
        lignes = liste_parent[i].split(separateur)
        for ligne in lignes:
            if ligne.startswith(startswith):
                new_list.append(ligne)
    return new_list 



def get_video_names(url_page):
    r = requests.get(url_page)
    
    soup = BeautifulSoup(r.content, "html5lib")

    # Cherche tous les liens sur la page
    liens = soup.findAll('a')

    # Texte à ignorer
    filtre = [  'Liste Animes',
                'Top Animes',
                'Films & Series',
                'Films',
                'Boutique',
                'Calendrier Sorties',
                'Partenaires',
                'Home',
                'Date',
                'Title',
                'Views',
                'Comments',
                'Date',
                'Title',
                'Views',
                'Comments', 
                'series-streaming'
             ]

    # Liste avec les liens 
    liste_lien = [lien.string for lien in liens if lien.string is not None and lien.string not in filtre]

    return liste_lien


def get_all_videos_name() -> set:
    animes_liste = list()
    i = 1
    url = f"https://wwv.voiranime.org/" # On regarde ce qu'il y a sur la page principale car si URL invalide on y est redirigé
                                        # Donc tant qu'on n'est pas redirigés -> la page numéro "n" existe.
    premiere_page = get_video_names(url)

    while True:
        url = f"https://wwv.voiranime.org/category/liste-animes/page/{i}/"
        page = get_video_names(url)

        if page[0] != premiere_page[0]:
            animes_liste.append(page)
            i += 1

        else:
            animes_set = set([val for sousliste in animes_liste for val in sousliste])
            print(f"Recherche terminée ! {len(animes_set)} animés ont été trouvés.\n")
            break


    return animes_set
