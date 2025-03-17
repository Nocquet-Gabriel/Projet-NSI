
from joueur import Joueur
from case import Case 
from personnage import Personnage
from question import Question
from plateau import Plateau
from tkinter import messagebox
from jeu import Jeu

a=input("Commencer le Jeu? [O/n]")
if a =="O" or a=="o":
    joueur1=Joueur("Kylian Descamps",17,"Brian")
    joueur2=Joueur("Ordi",9777,"Mo")
    jeu=Jeu(0,joueur1,joueur2)
    jeu.start()
    print(jeu.questions[1].caracteristiques)
    while not joueur1.gagne & joueur2.gagne==False:
        joueur1.PoserQuestion(jeu,)