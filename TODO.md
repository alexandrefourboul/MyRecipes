- Extraire ingrédients de liste ingrédients
- si ingrédient inexistant proposer de le rajouter
- lire quantité (et faire conversion)
- si modif sur recette refaire trourner ?
- Explorer de recettes ?
- changer icone
- base de données open food facts 




Questions:

1. Pour chaque ingredients dans une nouvelle recette : 
- requete pour savoir si elle existe dans la bdd si oui easy
- si non, recherche si un équivalent existe, si oui associer nouvelle équivalent
- si toujours pas nouvelle entrée 
est ce que cette enchainement de requete passe en terme de nombre de requetes BDD ??
  

2. si utilisation de open food facts : 
- https://fr.openfoodfacts.org/produit/3270160177387/4-dos-de-cabillaud-picard
https://fr.openfoodfacts.org/categorie/morues
par exemple dos de cabillaud n'existe pas en tant que catégorie
que en tant que produit fini(ce qui a priori nous intéresse pas)
donc il faudrait créer le noeud dos de cabillaud(ou arriver à comprendre comment le ratacher à open food facts)
- Pour info, open food facts france = 19809 catégories.
- Par contre si on travaille avec open food facts : possibilités de faire un extract des produits corresspondants pour une recette
avec les scores de chaque
- Ce qui serait intéressant c'est de découvrir comment se fait les liaisons entre noms de produits et catégories
je fouille la dedans pour en savoir plus : https://github.com/openfoodfacts/openfoodfacts-server
- https://github.com/openfoodfacts/openfoodfacts-python possibilté de faire des requêtes ici. Problème étant que la data source est centralisé sur le produit commercialisé alors que nous on ne cherche que les informations de catégories