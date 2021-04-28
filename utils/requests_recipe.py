req_add_recipe = """
INSERT INTO recipes
(title,time_prep,time_cook,difficulty,price,ingredients,tags,nb_people)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
"""

req_add_one_step = """
INSERT INTO recipe_steps
(recipe_id,order_step,step_verb,description,step_time,ingredients)
VALUES(%s,%s,%s,%s,%s,%s)
"""

req_add_one_ingredient = """
INSERT INTO ingredients
(name_ingredient,other_names,type_ingredient,price,comm)
VALUES(%s,%s,%s,%s,%s,%s)"""