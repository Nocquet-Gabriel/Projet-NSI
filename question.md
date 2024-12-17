# Classe Question

## Attributs

#### Question

l'attribut question est la chaine de caractères formant la question humaine posée lors du jeu de plateau. c'est celle qui sera affichée lors du jeu en tant qu'interface homme machine.

#### Caractéristiques

le programme n'étant pas capable de comprendre, de  répondre et d'agir  en fonction d'une chaine de Caractères , l'attribut caractéristiques, sous forme d'un tuple de tuples, lui permet de savoir quelles caractéristiques sont visées par la question, et donc éliminer les personnages en fonction. il est de la forme:

`((clé,effet),(clé,effet)) `

**clé** : clé du dictionnaire de caractéristiques de l'objet personnage

**effet** : l'effet permet de définir l'état d'un personnage en fonction de la réponse à la question. il y a 3 mots clés pour effet : True, False et None :

ce tableau résume les changements de l'état d'un personnage en fonction de l'effet

|                     | effet | *True* | *False* | *None*                  |
| ------------------- | ----- | -------- | --------- | ------------------------- |
| **réponse**  |       |          |           |                           |
| ***True***  |       | True     | False     | False                     |
| ***False*** |       | False    | True      | pas de changement d'état |

l'effet None est un cas spécifique : il agit comme un False lorsque la réponse est True, mais n'agit pas lorsque la réponse est False. il est utile dans les cas ou il y a plus de deux réponses possibles.
