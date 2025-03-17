from personnage import Personnage


class Question:
    def __init__(self, question: str, caractéristiques: tuple) -> None:
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
        self.answered=False
        

    def answer(self, reponse: bool, personnage: Personnage):
            # début de la boucle pour tous les tuples de caractéristiques
            for tuple1 in self.caracteristiques:
                if tuple1!=():
                    cle=tuple1[0]
                    effet=tuple1[1]
                    valeurRecherchee = not reponse ^ effet
                    # condition pour isoler les true et false
                    if effet != None:
                        # Plus Simplement : valeurRecherchee = reponse XNOR effet
                        # si la valeur de la caractéristique diffère de la valeur attendue, le personnage est éliminé (caché)
                        if personnage.caracteristiques[cle] != valeurRecherchee:
                            personnage.cache=True

                    else:
                        # si la valeur de la caractéristique est True, et que la réponse à la question est True, le personnage est éliminé (caché)
                        if reponse == True and personnage.caracteristiques[cle]:
                            personnage.cache=True
            self.answered=True
    def correspond(self):
        #vérifie qu'une question n'a pas déjà été posée
        if self.answered==False:
            return True
        return False
    
    def personnageCorrespond(self,personnage:Personnage):
        # peut être un time.sleep(1) pour pas que l'ordi réponde instant 
        if type(self.caracteristiques[0]) == tuple :
            cle = self.caracteristiques[0][0]
            reponseAttendue=self.caracteristiques[0][1]
        else :
            cle = self.caracteristiques[0]
            reponseAttendue=self.caracteristiques[1]
        reponsedelordi=None
        if personnage.caracteristiques[cle]==reponseAttendue:
            reponsedelordi='Oui'
            self.answered = True
        else:
            reponsedelordi='Non'
            self.answered = True
        return reponsedelordi
            