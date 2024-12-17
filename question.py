class Question:
    def __init__(self,question:str, caractéristiques:tuple) -> None:
        """créée l'instanciation de classe question : possède 3 attributs : une 
        question de type chaine de caractères, et les caractéristiques visées,
        sous la forme d'un tuple de tuples de la forme 
        (("caractéristique",effet),("caractéristique",effet))
        l'effet indique si la réponse à la question 
        va agir négativement 
        (False si la réponse est True, True si la réponse est False),
        positivement
        (True si la réponse est True, False si la réponse est False).
        ou semi-négativement (mot-clé = None)
        (False si la réponse est True, mais  ne remplace pas la valeur 
        existente si la réponse est False) (valeur = état personnage)
        --> mène à des questions additionnelles
        l'effet : True agit positivement et False 
        agit négativement"""
        self.question=question
        self.caracteristiques=caractéristiques