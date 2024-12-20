class Jeu:
    def __init__(self,difficulte:int,joueur1,joueur2) -> None:
        self.difficulte = difficulte
        self.joueur1=joueur1
        self.joueur2=joueur2
        self.plateau=None

    def start(self):
        q1 = Question("Est-ce une femme?", (("femme", True)))
        q2 = Question("a t-il/elle les cheveux longs?", (("cheveuxLongs", True)))
        q3 = Question("porte t-il/elle des lunettes?", (("lunettes", True)))
        q4 = Question("a-t-il/elle une moustache?", (("moustache", True)))
        q5 = Question("a t-il/elle les cheveux bouclés?",
              (("cheveuxBoucles", True), ("cheveuxLisses", False)))
        q6 = Question("porte t-il/elle un chapeau?"(("chapeau", True),
              ("casquette", None), ("bonnet", None)))
        q7 = Question("a-t-il/elle les yeux Bleus?", (("yeuxBleus", True),
              ("yeuxMarrons", None), ("yeuxVerts", None)))
        q8 = Question("a-t-il/elle les yeux Marrons?",
              (("yeuxMarrons", True), ("yeuxBleus", None), ("yeuxVerts", None)))
        q9 = Question("a-t-il/elle les yeux Verts?", (("yeuxVerts", True),
              ("yeuxMarrons", None), ("yeuxBleus", None)))
        q10 = Question("a-t-il/elle la peau claire?",
               (("peauClaire", True), ("peauMate", False)))
        q11 = Question("a-t-il/elle la peau mate?",
               (("peauMate", True), ("peauClaire", False)))
        q12 = Question("Porte t-il/elle des boucles d'oreilles?",
               (("BouclesOreilles", True)))
        q13 = Question("Porte t-il/elle une casquette",
               (("casquette", True), ("chapeau", None), ("bonnet", None)))
        q14 = Question("Porte t-il/elle un bonnet?", (("bonnet", True),
               ("chapeau", None), ("casquette", None)))
        q15 = Question("Semble t-il/elle souriant?",
               (("souriant", True), ("serieux", False)))
        q16 = Question("Semble t-il/elle sérieux?",
               (("serieux", True), ("souriant", False)))
        q17 = Question("semble t-il/elle vieux/vieille",
               (("vieux", True), ("jeune", False)))
        q18 = Question("semble t-il/elle jeune", (("jeune", True), ("vieux", False)))
