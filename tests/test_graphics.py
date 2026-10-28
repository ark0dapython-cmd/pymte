from pymte import graphics

regime = [750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500, 4750, 5000]
couple = [0, 20, 45, 70, 90, 110, 120, 128, 135, 142, 148, 147, 140, 132, 121, 117, 100, 87]

graphics.creer_graphique_2d("couple = f(regime)", regime, couple)