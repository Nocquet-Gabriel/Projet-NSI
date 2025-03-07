from joueur import Joueur
from case import Case 
from personnage import Personnage
from question import Question
from plateau import Plateau
from tkinter import messagebox
from jeu import Jeu    

joueur1=Joueur("Kylian Descamps",17,"Brian")
joueur2=Joueur("Ordi",9777,"Mo")
jeu=Jeu(0,joueur1,joueur2)
jeu.start()

assert jeu.questions[0].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'
assert jeu.questions[1].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'
assert jeu.questions[2].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[3].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[4].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[5].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[6].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[7].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'
assert jeu.questions[8].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[9].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'
assert jeu.questions[10].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[11].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[12].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[13].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[14].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'
assert jeu.questions[15].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[16].personnageCorrespond(jeu.persos["maggie"]) == 'Non'
assert jeu.questions[17].personnageCorrespond(jeu.persos["maggie"]) == 'Oui'

# print(len(jeu.questions[0].caracteristiques))