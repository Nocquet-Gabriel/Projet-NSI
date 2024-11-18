from tkinter import * 

fenetre = Tk()
label = Label(fenetre, text="Qui est-ce ?" ) 
label.pack()
value = StringVar() 
bouton1 = Radiobutton(fenetre, text="Hard", variable=value, value=1)
bouton2 = Radiobutton(fenetre, text="Medium", variable=value, value=2)
bouton3 = Radiobutton(fenetre, text="Easy", variable=value, value=3)
bouton1.pack()
bouton2.pack()
bouton3.pack()
fenetre.mainloop()