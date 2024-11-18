from tkinter import * 

fenetre = Tk()
#espace prévu pour créer du texte
label = Label(fenetre, text="Hello World", bg="Blue") 
label.pack()
#bouton
bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
# checkbutton
# bouton = Checkbutton(fenetre, text="Nouveau?")
bouton.pack()
# entrée
value = StringVar() 
# radiobutton
bouton1 = Radiobutton(fenetre, text="Oui", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Non", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Peut être", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
value.set("texte par défaut")
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()
fenetre.mainloop()
