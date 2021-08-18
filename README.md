# Anime-strime 
--------------------------------------------------------------------------------------------------------------------------------------  
## 1 - Organisation du projet 
--------------------------------------------------------------------------------------------------------------------------------------  

Menu pour choisir entre:  

1 - Regarder les animés disponibles  
2 - Reprendre avec le dernier animé  
3 - Entrer le nom d'un animé  

Choix 1 :  
    On peut proposer:  
        - une recherche des animés enregistrés (dans un fichier csv par exemple)  
        - de refaire une recherche -> implique de créer une fonction pour enregistrer les noms des animés (formatés) et le.s lien.s associé.s  

Choix 2:    
    On va récupérer le nom et numéro du dernier animé regardé -> implique:  
        - une fonction pour enregistrer nom et numéro de l'animé regardé  
        - une fonction pour lire ce fichier s'il existe  
        - une fonction pour faire la recherche via le nom recupéré dans le fichier   

Choix 3:  
    On va recupérer le nom entré et le formater de manière "le-nom-de-l-anime"  
    On fait ensuite une recherche dans le fichier csv -> il faut que les noms soient formatés dans le fichier   
    On utilisera la fonction recherche   

## 2 - Fonctions: 
--------------------------------------------------------------------------------------------------------------------------------------  

**On liste ici toutes les fonctions qu'on utilisera**

### 2.1 - Fonctions liées au Webscraping:


    - get_liens(url : str) -> List[str] 
        Fonction prenant en argument une url et retournant une liste de tous les liens menant aux vidéos trouvés sur cette page
    
    - get_nom_videos(url : str) -> set
        Fonction prenant en argument une url et renvoyant un set contenant les noms des animés disponibles sur le site 
        !! Il faudrait pouvoir trouver le lien associé à chaque nom d'animé également
    

### 2.2 - Fonctions liées aux fichiers:

    - write_episode(nom_anime: str, num_episode: str) -> None:
        Fonction prenant en argument le nom de l'animé ainsi que le numéro de l'épisode cherché

    - read_episode() -> str:
        Fonction lisant la dernière ligne du fichier où est stocké l'info sur le dernier épsiode regardé
        !! Au début on écrasera le fichier à chaque écriture, mais il serait bien par la suite de pouvoir conserver un historique des recherches
        !! et de n'afficher que la dernière ligne avec cette fonction, mais l'historique entier avec une autre 

    - save_episode(noms: list | set, urls: list | set) -> None:
        Fonctions prenant en argument les noms et urls et qui les enregistre dans un fichier csv
    
    - read_data(chemin: str) -> pandas.Dataframe:
        Fonction qui lit les données écrites dans le fichier csv et renvoie une Dataframe pandas 
    
    - cherche_anime(nom : str) -> str:
        Fonction qui cherche et renvoie l'url associée à un nom d'animé dans la dataframe 
        !! Si nom d'animé pas trouvé, proposer des noms proches à ceux entrés par l'utilisateur car certains noms longs peuvent ne pas être tapés en entier 
        !! On peut également proposer une liste des animés commençant par la même lettre

### 2.3 - Fonctions liées à la manipulation de texte:

    - formate_nom(nom : str) -> str:
        Fonction prenant en argument le nom entré par l'utilisateur et le formater telle que nom = "le-nom-de-l-anime"
    
    - deformate_nom(nom : str) -> str:
        Fonction faisant l'inverse de formate_nom. Elle renvoie un texte plus lisible à l'utilisateur 
    
### 2.4 - Fonctions liées à l'affichage:

    - print_ncol(ncol: int, objet: list | set) -> None:
        Affiche à l'écran un "print" reformaté mettant n colonnes côte à côte 
    

## 3 - Structure du projet
--------------------------------------------------------------------------------------------------------------------------------------  

On commence par les fonctions les plus basiques ne nécessitant aucun élément externe : 
    - Les fonctions de manipulation de texte 
    - Les fonctions d'affichage
     
    ---> On les positionne dans un paquet "utils"


Ensuite viennent les fonctions de manipulation de fichiers, dépendant des noms modifiés :
    ---> On les placera dans un fichier "fichiers.py"

Au-dessus encore, les fonctions liées au Webscraping, nécessitant les noms modifiées et données enregistrées :
    ---> On les placera dans un fichier "requetes.py"

Finalement, on aura un fichier "main.py" qui sera le point d'entré du programme

Pour schématiser : 


video-dl   
    |_____ main.py   
    |_____ requetes.py   
    |_____ fichiers.py   
    |_____ utils   
             |_____ __init__.py   
             |_____ texte.py   
             |_____ affichage.py   
    |_____ donnees  
             |_____ last_episode.txt   
             |_____ data.csv   

