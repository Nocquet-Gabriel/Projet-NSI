class Jeu:
    def __init__(self,difficulte:int,joueur1,joueur2) -> None:
        self.difficulte = difficulte
        self.joueur1=joueur1
        self.joueur2=joueur2
        self.plateau=None
