import os
from requetes import *
from getpass import getuser
from utils import *

def main() -> None:

    print(f"Bonjour {getuser()}, bienvenue sur video-flux !")
    num_episode = str()


    # Recherche le dernier épisode regardé
    if os.path.exists("episode.txt"):
        with open("episode.txt", "r") as r:
            print(f"Dernier épisode cherché : {r.read()}\n")
    else:
        print("Aucun épisode en mémoire")

    while len(num_episode) < 1:
        num_episode = input("Numéro de l'épisode à regarder : ")

    url = f"https://wwv.voiranime.org/my-hero-academia-saison-5-episode-{num_episode}-vostfr/"
    
    
    with open("episode.txt", "w") as f:
        f.write(num_episode)
    
    extensions_photo = ["jpg", "png", "gif"]
    liens = get_video_links(url)

    #print("Liens récupérés, récupération des balises 'src'")
    src = tri_balise(liens, "src")
    #print("Balises 'src' triées, récupération des liens vidéos ...\n")
    https_links = tri_balise(liste_parent=src, startswith="https", separateur='"')
    videos = [http for http in https_links if http[-3:] not in extensions_photo]
    
    print("\n Possibles liens des vidéos : \n")
    print_liste(videos)


if __name__ == "__main__": 
    main()
