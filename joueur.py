from random import randint
from personnage import Personnage
from question import Question
class Joueur:
    def __init__(self,nom:str,age:int,diff:int,personnage:Personnage) -> None:
        self.nom=nom
        self.age=age
        self.nbPartiesGagnées=0
        self.DifficulteChoisie=diff
        self.personnageSelectionne=personnage

    def selectionPersonnage(perso:Personnage):
        pass

class Ordi:
    def __init__(self,nom:str,personnage:Personnage,diff:int) -> None:
        super().__init__(nom,randint(3,50),diff,personnage)