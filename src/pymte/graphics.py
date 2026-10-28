#   =============================
#             imports
#   =============================

import matplotlib.pyplot as plt
import numpy as np

#   =============================
#               Code
#   =============================

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