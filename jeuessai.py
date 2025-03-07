
from joueur import Joueur
from case import Case 
from personnage import Personnage
from question import Question
from plateau import Plateau
from tkinter import messagebox
from jeu import Jeu

a=input("Commencer le Jeu? [O/n]")
if a =="O" or a=="o":
    joueur1=Joueur("Kylian Descamps",17,)
    jeu=Jeu(0,)