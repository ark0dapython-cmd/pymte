from pymte import fuel

while True :
    try :
        carbone = int(input("Nombre de Carbone --> "))
        fuel.valider_carbone(carbone)
        break
    except ValueError as erreur:
        print(erreur)

while True :
    try :
        hydrogene = int(input("Nombre d'atomes d'hydrogène --> "))
        fuel.valider_hydrogene(hydrogene)
    except ValueError as erreur:
        print(erreur)

while True :
    try :
        oxygene = int(input("Nombre d'atomes d'oxygène --> "))
        fuel.valider_oxygene(oxygene)
    except ValueError as erreur:
        print(erreur)

fuel.analyse_carburant(carbone, hydrogene, oxygene)