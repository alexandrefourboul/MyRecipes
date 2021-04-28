source = "https://lacerisesurlemaillot.fr/blanquette-cabillaud/"
nb_people = 4
time_prep = 15
time_cook = 60

"""
600 g de dos de cabillaud en 4 pavés
400 g de petites pommes de terre
200 g de champignons de Paris
300 g de carottes
1 poireau
1 échalote
20 cl de crème liquide
Le jus d’1 citron
1 jaune d’œuf
180 g de vin blanc sec 200ml
400 g d’eau 400ml
1 cube de bouillon de légumes bio
1 cuillère à soupe d’huile d’olive
20 g de farine
Sel
Poivre
Persil"""
json_ing = {
    'dos de cabillaud': [600, 'g'],
    'petites pommes de terre': [400, 'g'],
    'champignons de paris': [200, 'g'],
    'carottes': [300, 'g'],
    'poireau': [1, 'unit'],
    'echalote': [1, 'unit'],
    'crème liquide': [20, 'cl'],
    'jus de citron': [1, 'unit'],
    "jaune d'oeuf": [1, 'unit'],
    'vin blanc sec': [200, 'ml'],
    'eau': [400, 'ml'],
    'cube de bouillon de légume': [1, 'unit'],
    "huile d'olive": [1, 'CS'],
    'farine': [20, 'g'],
    'sel': [],
    'poivre': [],
    'persil': []
}

ingredients = [k for k in json_ing.keys()]

steps = """Éplucher les pommes de terre.
Couper la barbe et le vert trop dur du poireau, enlever sa première peau, le rincer.
Couper les extrémités des carottes, les éplucher.
Tailler poireau et carottes en tronçons d’environ 1 cm d’épaisseur.
Peler et émincer l’échalote, la faire revenir dans une cocotte 1 minute à feu vif avec 1 cuillère à soupe d’huile d’olive.
Ajouter les carottes et poireaux et poursuivre la cuisson 5 minutes à feu moyen en remuant régulièrement.
Saupoudrer la farine et cuire encore 1 minute en remuant.
Verser le vin blanc, mélanger et laisser évaporer 1 minute à feu vif.
Ajouter le cube de bouillon, les pommes de terre, verser l‘eau et porter à ébullition, couvrir et laisser mijoter pendant 40 minutes en remuant de temps en temps.
Nettoyer les champignons, les couper en 2 ou en 4 selon leur grosseur. Les ajouter à la blanquette et poursuivre la cuisson 5 minutes. Saler et mettre quelques tours de moulin à poivre.
Pendant ce temps, cuire les pavés de cabillaud 10 minutes à la vapeur.
Fouetter à la fourchette la crème avec le jus de citron et le jaune d’œuf.
Ajouter ce mélange à la blanquette, couper le feu et remuer.
Dresser : servir la blanquette dans 4 assiettes creuses et déposer le pavé de cabillaud dessus. Mettre un peu de fleur de sel, quelques tours de poivre du moulin et parsemer de persil ciselé."""

split_steps = steps.split('.')
# [id_recipe, order, verb, description, step_time, ingredients
split_steps = [
    [1, i + 1] +
    split_steps[i].split(maxsplit=1) +
    [{ing: [] for ing in json_ing.keys() if ing in split_steps[i]},
                                                     None]
    for i in range(len(split_steps)) if split_steps[i]
]
