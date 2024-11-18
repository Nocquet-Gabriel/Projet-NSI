from personnage import Personnage
class Case:
    def __init__(self,personnage:Personnage) -> None:
        self.ouvert=True
        self.personnageAssocie=personnage
