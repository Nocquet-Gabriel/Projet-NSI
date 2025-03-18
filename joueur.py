from random import randint
from personnage import Personnage
from question import Question
from jeu import Jeu

class Joueur:
    def __init__(self,nom:str,age:int,personnage:str,Ordi=False) -> None:
        self.nom=nom
        self.age=age
        self.nbPartiesGagnées=0
        self.personnageSelectionne=personnage
        self.gagne=False
        self.ordi=Ordi

    def PoserQuestion(self, jeu, q:int):
        if self.ordi == False:
            question= jeu.questions[q]
            print(question.question)
            reponse = question.personnageCorrespond(jeu.persos[self.personnageSelectionne.lower()])
            print(reponse)
        else:
            question= jeu.questions[q]
            print(question.question)
            a=input("Votre Réponse (Oui/Non): ")
            if a=="Oui" or a=="oui":
                for key in jeu.persos.keys():
                    perso = jeu.persos[key]
                    question.answer(True,perso)
            else:
                for key,val in jeu.persos.items():
                    perso = jeu.persos[key]
                    question.answer(False,perso)
                    