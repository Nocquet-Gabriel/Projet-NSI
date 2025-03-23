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
            # print(question.question)
            reponse = question.personnageCorrespond(jeu.persos[self.personnageSelectionne.lower()])
            print(reponse)
        else:
            question= jeu.questions[q]
            print(question.question)
            reponse=input("Votre Réponse (Oui/Non): ")
            if reponse=="Oui" or reponse=="oui":
                for key in jeu.persos.keys():
                    perso = jeu.persos[key]
                    question.answer(True,perso)
            else:
                for key,val in jeu.persos.items():
                    perso = jeu.persos[key]
                    question.answer(False,perso)
    

    def DevinerPersonnage(self, jeu:Jeu, personnage:Personnage, joueur2): # Quoi qu'il arrive, cette fonction met fin au jeu.
        """Quoi qu'il arrive, cette fonction met fin au jeu, elle permet de demander au joueur adverse si 
        le personnage à deviner est bien celui donné en paramètre. le joueur gagne si c'est le bon personnage,
        et perd si ce n'est pas le bon"""
        question = f"est-ce {personnage.nom} ?"
        reponse = None
        if joueur2.personnageSelectionne == personnage.nom:
            reponse = 'Oui'
            self.gagne = True # cet attribut Met fin au jeu, le joueur a gagné
        else :
            reponse = 'Non'
            joueur2.gagne = True #cet attribut met fin au jeu, le joueur a perdu
