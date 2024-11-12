class Joueur:
    def __init__(self,nom,age,diff) -> None:
        self.nom=nom
        self.age=age
        self.nbPartiesGagnées=0
        self.DifficulteChoisie=diff
class Ordi:
    def __init__(self,nom="Ordi",diff=1) -> None:
        super().__init__(nom,diff)