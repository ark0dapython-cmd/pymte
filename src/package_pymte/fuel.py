def composition_molecule(c = 0, h = 0, o = 0):

    """
    Cette fonction permet de calculer la composition d'une molécule à partir :

    - du nombre d'atomes de carbone (c)
    - du nombre d'atomes d'hydrogène (h)
    - du nombre d'atomes d'oxygène (o)

    Elle retourne un dictionnaire contenant la composition de la molécule avec les clés 'C', 'H', et 'O'.
    """
    compo_carb = {'C': c, 'H': h, 'O': o}
    return compo_carb


def afficher_molecule(c = 0, h = 0, o = 0):

    """
    Cette fonctione permet de créer une molécule a partir :

    - du nombre d'atomes de carbone (c)
    - du nombre d'atomes d'hydrogène (h)
    - du nombre d'atomes d'oxygène (o)

    Elle retourne une F-string représentant la molécule sous la forme "C{c}H{h}O{o}".
    """

    return f"C{c}H{h}O{o}"

