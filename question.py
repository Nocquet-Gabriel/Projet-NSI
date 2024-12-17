from personnage import Personnage


class Question:
    def __init__(self, question: str, caractéristiques: list) -> None:
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
        self.question = question
        self.caracteristiques = caractéristiques

    def answer(self, reponse: bool, personnage: Personnage):
            # début de la boucle pour tous les tuples de caractéristiques
            for liste in self.caracteristiques:
                # On isole la clé et l'effet
                    for cle,effet in liste:            
                        valeurRecherchee = not reponse ^ effet
                        # condition pour isoler les true et false
                        if effet != None:
                            # Plus Simplement : valeurRecherchee = reponse XNOR effet
                            # si la valeur de la caractéristique diffère de la valeur attendue, le personnage est éliminé (caché)
                            if personnage.caracteristiques[cle] != valeurRecherchee:
                                personnage.cacher()

                        else:
                            # si la valeur de la caractéristique est True, et que la réponse à la question est True, le personnage est éliminé (caché)
                            if reponse == True and personnage.caracteristiques[cle]:
                                personnage.cacher()


q1 = Question("Est-ce une femme?",([["femme",True]])
emma = Personnage("Emma",True,True,False,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False)
print(emma.cache)

q1.answer(False,emma)

print(emma.cache)