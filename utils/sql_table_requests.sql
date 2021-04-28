CREATE TABLE public.recipes (
	id_recipe serial NOT NULL,
	title varchar NOT NULL,
	time_prep smallint NOT NULL,
	time_cook smallint NULL,
	difficulty smallint NULL,
	price smallint NULL,
	ingredients json NOT NULL,
	tags _varchar NULL,
	nb_people smallint NOT NULL,
	comm varchar NULL,
	CONSTRAINT recipes_pk PRIMARY KEY (id_recipe)
);



CREATE TABLE public.ingredients (
	id_ingredient serial NOT NULL,
	name_ingredient varchar NOT NULL,
	other_names _varchar NULL,
	type_ingredient varchar NULL,
	price smallint NULL,
	comm varchar NULL,
	CONSTRAINT ingredients_pk PRIMARY KEY (id_ingredient)
);


CREATE TABLE public.recipe_steps (
	id_step serial NOT NULL,
	recipe_id serial NOT NULL,
	order_step smallint NOT NULL,
	step_verb varchar NOT NULL,
	step_time smallint NULL,
	ingredients json NULL,
	CONSTRAINT recipe_steps_pk PRIMARY KEY (id_step),
	CONSTRAINT recipe_steps_fk FOREIGN KEY (recipe_id) REFERENCES public.recipes(id_recipe)
);


CREATE TABLE public.step_verbs (
	id_verb serial NOT NULL,
	verb varchar NOT NULL,
	description varchar NULL,
	equipments _varchar NULL,
	CONSTRAINT step_verbs_pk PRIMARY KEY (id_verb)
);

CREATE TABLE public.equipments (
	id_equipment serial NOT NULL,
	name_equipment varchar NOT NULL,
	other_names _varchar NULL,
	available boolean NULL,
	recipe_ids _int2 NULL,
	comm varchar NULL,
	CONSTRAINT equipments_pk PRIMARY KEY (id_equipment)
);

