from random import randint
from personnage import Personnage
from question import Question
class Joueur:
    def __init__(self,nom:str,age:int,personnage:str) -> None:
        self.nom=nom
        self.age=age
        self.nbPartiesGagnées=0
        self.personnageSelectionne=personnage
        self.gagne=False

    def PoserQuestion(self, jeu, q):
        print(jeu.questions[q].question)
        