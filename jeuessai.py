
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
    while not joueur1.gagne and not joueur2.gagne:
        joueur1.PoserQuestion(jeu,2)
        
        b=input("END")
        joueur1.gagne=True