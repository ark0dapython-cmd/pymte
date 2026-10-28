#   =============================
#               Code
#   =============================

# ===== Affichage de la molécule =====
def afficher_molecule(c = 0, h = 0, o = 0):

    """
    Cette fonctione permet de créer une molécule a partir :
²
    - du nombre d'atomes de carbone (c)
    - du nombre d'atomes d'hydrogène (h)
    - du nombre d'atomes d'oxygène (o)

    Elle retourne une F-string représentant la molécule sous la forme "C{c}H{h}O{o}".
    """
    if o == 0 :
        return f"C{c}H{h}"
    elif o == 1 :
        return f"C{c}H{h}O"
    else :
        return f"C{c}H{h}O{o}"

# ===== Création des coefficients de l'équation stoechiométrique =====
def creer_equation_stoechiometrique(c, h, o):
    """
    Cette focntion permet de créer les coefficients de l'équation stoechiométrique du carburant a partir :

    - du nombre d'atomes de carbone (c)
    - du nombre d'atomes d'hydrogène (h)
    - du nombre d'atomes d'oxygène (o)

    Elle retourne les coefficient d'air de CO2, d'H2O et de N2
    """
    global coef_co2
    global coef_h2o
    global coef_air
    global coef_n2

    coef_co2 = c
    coef_h2o = round(h/2, 2)

    if o == 0 :
        coef_air = c + (h/4)
    else :
        coef_air = c + (h/4) - (o/2)
    coef_n2 = coef_air * 3.78

    return coef_co2, coef_h2o, coef_air, coef_n2


# ===== Affichage visuelle de l'équation stoechiométrique =====
def afficher_equation_stoechiometrique(c, h, o):
    """
    Cette fonction permet l'affichage de l'équation crée via la fonction creer_equation_stoechiometrique.

    Elle retourne l'équation stoechiométrique sous forme de F-string.
    """
    global coef_co2
    global coef_h2o
    global coef_air
    global coef_n2
    
    return f"{afficher_molecule(c, h, o)} + {coef_air} (O2 + 3.78 N2) --> {coef_co2} CO2 + {coef_h2o} H2O + {coef_n2} N2"

# ===== Calcul des masses autour du carburant =====
def calculs_masses(c, h, o):
    """
    Cette fonction permet de calculer les différentes masses de carburant, d'air, de co2, d'h2o et de n2 a partir de l'équation de combustion.

    Elle renvoie des masses sous forme de F-strings.
    """

    global masse_co2
    global masse_h2o
    global masse_air
    global masse_carburant
    global masse_o2
    global masse_n2
    
    masse_carburant = round(c * M_C + h * M_H + o * M_O, 3)
    masse_co2 = round(coef_co2 * (M_C + 2 * M_O), 3)
    masse_h2o = round(coef_h2o * (2 * M_H + M_O), 3)
    masse_air = round(coef_air * (2 * M_O + 2 * 3.78 * M_N), 3)
    masse_o2 = round(coef_air * (2 * M_O), 3)
    masse_n2 = round(coef_n2 * M_N, 3)

    return masse_co2, masse_h2o, masse_air, masse_carburant, masse_o2, masse_n2

# ===== Calcul de la répartition de carbone, hydrogène et oxygène dans le carburant =====
def calcul_repartition_carburant(c, h, o):
    """
    Cette fonction permet de calculer la répartition des éléments dans le carburant.
    """
    global repart_carbone
    global repart_hydrogene
    global repart_oxygene
    global masse_carburant

    repart_carbone = round((c * M_C) / masse_carburant * 100, 3)
    repart_hydrogene = round((h * M_H) / masse_carburant * 100, 3)

    if o == 0 :
        repart_oxygene = "/"
    else :
        repart_oxygene = round((o * M_O) / masse_carburant * 100, 3)

    return repart_carbone, repart_hydrogene, repart_oxygene



# ===== Calcul du rapport Air/Fuel stoechiométrique =====
def calcul_rapport_af():
    """
    Cette fonction permet de déterminer le rapport Air/Fuel d'un carburant a partir de la masse d'air et de la masse de carburant.

    Elle renvoie la variable rapport_af
    """
    global masse_air
    global masse_carburant
    global rapport_af

    rapport_af = round(masse_air/masse_carburant, 3)

    return rapport_af

# ===== Calcul du rapport H/C stoechiométrique =====
def calcul_rapport_h_c(h, c):
    """
    Cette fonction permet de déterminer le rapport H/C d'un carburant a partir du nombre d'atomes d'hydrogène et de carbone.

    Elle renvoie la variable rapport_hc
    """
    global rapport_h_c

    rapport_h_c = round(h/c, 3)

    return rapport_h_c

# ===== Calcul du rapport O/C stoechiométrique =====
def calcul_rapport_o_c(o, c):
    """
    Cette fonction permet de déterminer le rapport O/C d'un carburant a partir du nombre d'atomes d'oxygène et de carbone.

    Elle renvoie la variable rapport_o_c
    """
    global rapport_o_c

    if o == 0 :
        rapport_o_c = "/"
    else :
        rapport_o_c = round(o/c, 3)

    return rapport_o_c

def calcul_facteur_massique():
    """
    Cette fonction permet de calculer le facteur massique de CO2 et H2O a partir de la masse de carburant, de CO2 et d'H2O.

    Elle renvoie les variables facteur_massique_co2 et facteur_massique_h2o
    """
    global masse_carburant
    global masse_co2
    global facteur_massique_co2
    global facteur_massique_h2o

    facteur_massique_co2 = round(masse_co2/masse_carburant, 3)
    facteur_massique_h2o = round(masse_h2o/masse_carburant, 3)

    return facteur_massique_co2, facteur_massique_h2o

def calcul_composition_gaz():
    """
    Cette fonction permet de calculer la composition des gazs a partir de la masse de CO2, H2O et N2.

    Elle renvoie les variables compo_co2, compo_h2o et compo_n2
    """
    global masse_co2
    global masse_h2o
    global masse_n2
    global compo_gaz_co2
    global compo_gaz_h2o
    global compo_gaz_n2

    total_masse_gaz = masse_co2 + masse_h2o + masse_n2

    compo_gaz_co2 = round(masse_co2/total_masse_gaz * 100, 3)
    compo_gaz_h2o = round(masse_h2o/total_masse_gaz * 100, 3)
    compo_gaz_n2 = round(masse_n2/total_masse_gaz * 100, 3)

    return compo_gaz_co2, compo_gaz_h2o, compo_gaz_n2

#   =============================
#   Fonction de l'affichage final
#   =============================
 
def analyse_carburant(c, h, o):
    creer_equation_stoechiometrique(c, h, o)
    calculs_masses(c, h, o)
    calcul_repartition_carburant(c, h, o)
    calcul_rapport_af()
    calcul_rapport_h_c(h, c)
    calcul_rapport_o_c(o, c)
    calcul_facteur_massique()
    calcul_composition_gaz()

    print("==========ANALYSE DU CARBURANT==========")
    print(f"\nMolecule : {afficher_molecule(c, h, o)}")
    print(f"Equation Stoechiometrique : {afficher_equation_stoechiometrique(c, h, o)}")
    print("\n--- Composition du carburant ---")
    print(f"  > Masse carburant : {masse_carburant} g \n  > %Carbone : {repart_carbone} % \n  > %Hydrogene : {repart_hydrogene} % \n  > %Oxygene : {repart_oxygene} % \n  > Rapport H/C : {rapport_h_c} \n  > Rapport O/C : {rapport_o_c}")
    print("--- Air & Stoechiometrie ---")
    print(f"  > Besoin en O2 : {coef_air} mol \n  > Masse de O2 : {masse_o2} g \n  > Masse d'air : {masse_air} g \n  > Rapport Air/Fuel : {rapport_af}")
    print("--- Produits de la combustion ---")
    print(f"  > Masse de CO2 : {masse_co2} g \n  > Masse de H2O : {masse_h2o} g \n  > Masse de N2 : {masse_n2} g \n  > facteur massique CO2 : {facteur_massique_co2} \n  > facteur massique H2O : {facteur_massique_h2o}")
    print("--- Composition des gazs---")
    print(f"  > CO2 : {compo_gaz_co2} % \n  > H2O : {compo_gaz_h2o} % \n  > N2 : {compo_gaz_n2} %")
    print("========================================")

# VARIABLES GLOBALES
M_C = 12 #g/mol
M_H = 1 #g/mol
M_O = 16 #g/mol
M_N = 14 #g/mol