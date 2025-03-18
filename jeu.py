from question import Question
from personnage import Personnage
class Jeu:
    def __init__(self,difficulte:int,joueur1,joueur2) -> None:
        self.difficulte = difficulte
        self.joueur1=joueur1
        self.joueur2=joueur2
        self.plateau=None
        self.questions=[]
        self.persos=None

    def start(self):
        #Instanciation des questions
        q1 = Question("Est-ce une femme?", 
                    (("femme", True)))

        q2 = Question("a t-il/elle les cheveux longs?", 
                    (("cheveuxLongs", True)))

        q3 = Question("porte t-il/elle des lunettes?", 
                    (("lunettes", True)))

        q4 = Question("a-t-il/elle une moustache?", 
                    (("moustache", True)))

        q5 = Question("a t-il/elle les cheveux bouclés?",
                    (("cheveuxBoucles", True), ("cheveuxLisses", False)))

        q6 = Question("porte t-il/elle un chapeau?",
                    (("chapeau", True),("casquette", None), ("bonnet", None)))

        q7 = Question("a-t-il/elle les yeux Bleus?", 
                    (("yeuxBleus", True),("yeuxMarrons", None), ("yeuxVerts", None)))

        q8 = Question("a-t-il/elle les yeux Marrons?",
                    (("yeuxMarrons", True), ("yeuxBleus", None), ("yeuxVerts", None)))

        q9 = Question("a-t-il/elle les yeux Verts?", 
                    (("yeuxVerts", True),("yeuxMarrons", None), ("yeuxBleus", None)))

        q10 = Question("a-t-il/elle la peau claire?",
                    (("peauClaire", True), ("peauMate", False)))

        q11 = Question("a-t-il/elle la peau mate?",
                    (("peauMate", True), ("peauClaire", False)))

        q12 = Question("Porte t-il/elle des boucles d'oreilles?",
                    (("BouclesOreilles", True)))

        q13 = Question("Porte t-il/elle une casquette",
                    (("casquette", True), ("chapeau", None), ("bonnet", None)))

        q14 = Question("Porte t-il/elle un bonnet?", 
                    (("bonnet", True),("chapeau", None), ("casquette", None)))

        q15 = Question("Semble t-il/elle souriant?",
                    (("souriant", True), ("serieux", False)))

        q16 = Question("Semble t-il/elle sérieux?",
                    (("serieux", True), ("souriant", False)))

        q17 = Question("semble t-il/elle vieux/vieille",
                    (("vieux", True), ("jeune", False)))

        q18 = Question("semble t-il/elle jeune", 
                    (("jeune", True), ("vieux", False)))

        self.questions.append(q1)
        self.questions.append(q2)
        self.questions.append(q3)
        self.questions.append(q4)
        self.questions.append(q5)
        self.questions.append(q6)
        self.questions.append(q7)
        self.questions.append(q8)
        self.questions.append(q9)
        self.questions.append(q10)
        self.questions.append(q11)
        self.questions.append(q12)
        self.questions.append(q13)
        self.questions.append(q14)
        self.questions.append(q15)
        self.questions.append(q16)
        self.questions.append(q17)
        self.questions.append(q18)

# Instanciation des personnages (sous forme de dictionnaire)
       self.persos={
           "basil": Personnage("Basil", False, False, False, False, False, True, False, False,
                              True, False, True, False, False, False, False, True, True, False, False),
           "bill": Personnage("Bill",False,False,False,True,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "brian": Personnage("Brian",False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False),

           "edna": Personnage("Edna",True,True,True,False,False,True,False,False,False,True,True,False,False,False,False,True,False,True,False),

           "gary": Personnage("Gary",False, False,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,True),

           "hannah": Personnage("Hannah",True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "ian": Personnage("Ian",False,False,True,True,False,True,False,False,True,False,True,False,False,False,False,True,False,True,False),

           "isla" : Personnage("Isla",True,True,False,False,True,False,False,False,False,True,True,False,False,False,False,True,True,False,False),

           "jennifer" : Personnage("Jennifer",True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "joshua" : Personnage("Joshua",False,False,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "kelly" : Personnage("Kelly", True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False),

           "kim" : Personnage("Kim",True,True,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "maggie" : Personnage("Maggie",True,True,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "martine" : Personnage("Martine",True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "melvin" : Personnage("Melvin", False,False,True,False,False,True,False,True,False,False,True,False,False,False,False,True,True,False,False),

           "mo" : Personnage("Mo",False,False,False,True,False,True,True,False,True,False,True,False,False,False,False,True,True,False,False),

           "natalie" : Personnage("Natalie", True,True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False),

           "pete" : Personnage("Pete", False, False,False,True,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "roy" : Personnage("Roy", False,False,True,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "rupert" : Personnage("Rupert",False,False,True,True,False,True,False,False,False,True,True,False,False,False,False,True,True, False, False),

           "simone" : Personnage("Simone", True, True,False,False,False,True,False,False,False,True,True,False,False,False,False,True,True,False,False),

           "stephen" : Personnage("Stephen",False,False,False,False,False,True,False,False,True,False,False,True,False,False,False,True,True,False,False),

           "susan" : Personnage("Susan", True,False,False,False,True,False,False,False,True,False,True,False,False,False,False,True,True,False,False),

           "xiaomei" : Personnage("Xiao Mei",True,True,False,False,False,True,False,False,True,False,True,False,False,False,False,True,True,False,False)
       }