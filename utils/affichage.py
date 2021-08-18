import os 
import sys 

def print_ncol(n, liste):
    col, lin = os.get_terminal_size()
    liste = sorted(list(liste))  # Le set n'est plus trié une fois passé en argument (pourquoi ?)
    print(col * "=")
    print((col/2 - 7) * " ", "Liste des animés") # -7 car le texte ensuite fait 15 caractères (on pourrait len(texte)//2 sinon ...)
    print(col * "=")
    for i, anim in enumerate(liste):
        if i % n != 0:
            print(f"{i: <2d} - {anim : <70s}", end="")
        else:
            print(f"{i} - {anim}", end="\n")

def print_liste(liste):
    for i, item in enumerate(liste):
        print(f"{i + 1} - {item}\n")

# def print_tri_col(liste):
#     l = len(list)
#     indice = int(l/3)
#     c1, c2, c3 = liste[:indice], liste[indice : 2*indice], liste[2*indice:]

#     for i, j, k in zip(c1, c2, c3):
#         print(i)

# choix = True
# pos = [False, True]
# while choix:
#     a = int(input("Colonnes : "))
#     b = int(input("Lignes :"))

#     if sys.platform.startswith("linux"):
#         cmd = f"resize -s {b} {a}; stty rows {b}; stty cols {a}"
#         os.system(cmd)

#     elif sys.platform.startswith("win32"):
#         cmd = f'mode {a}, {b}'
#         os.system(cmd)

#         couleur = input("Couleur :")
#         com = f'color {couleur}'
#         os.system(com)
#     elif sys.platform.startswith("darwin"):
#         print("Looser de Mac OS")
        
#     index = int(input("Continuer ? (0/1)"))
#     choix = pos[index]

