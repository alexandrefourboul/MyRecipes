
from mdutils.mdutils import MdUtils
from mdutils import Html


class Recipe:

    def __init__(self, preparation_duration, baking_duration, ingredients):
        self.name = name
        self.preparation_duration = preparation_duration
        self.baking_duration = baking_duration
        self.total_duration = self.preparation_duration + self.baking_duration
        self.ingredients = self.ingredients_association(ingredients)

    def ingredients_association(self):
        return 0

    def recipe_to_file(self, files_path):
        mdFile = MdUtils(file_name=self.name, title=self.name)
        mdFile.new_header(level=1, title='Ingredients')
        #TODO liste et quantité des ingrédients
        mdFile.new_header(level=1, title='Preparation')
        #TODO étape de la recette, 1,2 ,3 

        return 0
