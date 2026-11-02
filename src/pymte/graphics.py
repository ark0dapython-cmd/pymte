#   =============================
#             imports
#   =============================

import matplotlib.pyplot as plt
import numpy as np

#   =============================
#               Code
#   =============================

def verification_conformite_2d(liste1, liste2):
    """
    Cette fonction permet de vérifier la conformité de 2 listes sur les caractériques suivantes :

    - même longueur
    - listes non vides

    Elle renvoie True si les 2 listes sont conformes, sinon elle renvoie False
    """
    if len(liste1) != len(liste2):
        return False
    elif liste1 == [] or liste2 == [] :
        return False
    else :
        return True

def creer_graphique_2d(name, axe_x, axe_y):
    """
    Cette fonction permet de créer et afficher un graphique 2D a partir de deux axes donnés :

    - axe_x : Axe des abscisses (liste ou tableau de valeurs)
    - axe_y : Axe des ordonnées (liste ou tableau de valeurs)
    """
    plt.plot(axe_x, axe_y)
    plt.xlabel("")
    plt.ylabel("")
    plt.title(name)
    plt.grid()
    plt.show()