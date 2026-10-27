def creemolecule(c = 0, h = 0, o = 0):

    """
    Cette fonctione permet de créer une molécule a partir :

    - du nombre d'atomes de carbone (c)
    - du nombre d'atomes d'hydrogène (h)
    - du nombre d'atomes d'oxygène (o)

    Elle retourne une F-string représentant la molécule sous la forme "C{c}H{h}O{o}".
    """

    return f"C{c}H{h}O{o}"

