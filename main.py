from tkinter import *

from joueur import Joueur

from case import Case

from personnage import Personnage

from question import Question

from plateau import Plateau

#Instanciation des questions NE PAS TOUCHER POUR LE MOMENT

q1=Question("Est-ce une femme?",(("Femme",True)))
q2=Question("a t-il/elle les cheveux longs?",(("cheveuxLongs",True)))
q3=Question("porte t-il/elle des lunettes?",(("lunettes",True)))
q4=Question("a-t-il/elle une moustache?",(("moustache",True)))
q5=Question("a t-il/elle les cheveux bouclés?",(("cheveuxBoucles",True),("cheveuxLisses",False)))
q6=Question("porte t-il/elle un chapeau?"(("chapeau",True),("casquette",None),("bonnet",None)))
q7=Question("a-t-il/elle les yeux Bleus?",(("yeuxBleus",True),("yeuxMarrons",None),("yeuxVerts",None)))
q8=Question("a-t-il/elle les yeux Marrons?",(("yeuxMarrons",True),("yeuxBleus",None),("yeuxVerts",None)))
q9=Question("a-t-il/elle les yeux Verts?",(("yeuxVerts",True),("yeuxMarrons",None),("yeuxBleus",None)))
q10=Question("a-t-il/elle la peau claire?",(("peauClaire",True),("peauMate",False)))
q11=Question("a-t-il/elle la peau mate?",(("peauMate",True),("peauClaire",False)))
q12=Question("Porte t-il/elle des boucles d'oreilles?",(("BouclesOreilles",True)))
q13=Question("Porte t-il/elle une casquette",(("casquette",True),("chapeau",None),("bonnet",None)))
q14=Question("Porte t-il/elle un bonnet?",(("bonnet",True),("chapeau",None),("casquette",None)))
q15=Question("Semble t-il/elle souriant?",(("souriant",True),("serieux",False)))
q16=Question("Semble t-il/elle sérieux?",(("serieux",True),("souriant",False)))
q17=Question("semble t-il/elle vieux/vieille",(("vieux",True),("jeune",False)))
q18=Question("semble t-il/elle jeune",(("jeune",True),("vieux",False)))

#Interface du Menu

root = Tk()  # create root window
root.title("Qui-est-ce ?")
root.iconbitmap("QEC_Logo.ico")
root.config(bg="dodgerblue")

# Set the window icon
# root.iconbitmap('path_to_icon.ico')

# Create Frame widget
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

# Create frame within left_frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Load logo
image = PhotoImage(file="QEC_Logo.png")
original_image = image.subsample(3, 3)  # resize image
Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

# Function to open a new window with a message for solo


def on_button_solo():
    new_window = Toplevel(root)
    new_window.title("Solo")
    new_window.geometry("700x600")  # resize window
    new_window.iconbitmap("QEC_Logo.ico")
    # Load logo
    logo = PhotoImage(file="QEC_Logo.png")
    logo_label = Label(new_window, image=logo)
    logo_label.image = logo  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)
    Label(new_window, text="Choose your difficulty").pack(padx=20, pady=20)
    # Add new buttons to the new window
    buttonHard = Button(new_window, text="Hard", command=not_available)
    buttonHard.pack(pady=10)
    buttonMedium = Button(new_window, text="Medium", command=not_available)
    buttonMedium.pack(pady=10)
    buttonEasy = Button(new_window, text="Easy")
    buttonEasy.pack(pady=10)

# Function to display "Not available yet" message


def not_available():
    new_window = Toplevel(root)
    new_window.iconbitmap("QEC_Logo.ico")
    new_window.title("Not available")
    Label(new_window, text="Not available yet").pack(padx=20, pady=20)

# Function to close the window


def quit_app():
    root.quit()

# Function to open a new window with a message


def on_button_multiplayer():
    new_window = Toplevel(root)
    new_window.title("Multiplayer")
    new_window.iconbitmap("QEC_Logo.ico")
    Label(new_window, text="Multiplayer not available yet").pack(padx=20, pady=20)


# Create buttons and place them under the logo
buttonSolo = Button(left_frame, text="Solo", command=on_button_solo)
buttonSolo.grid(row=1, column=0, padx=5, pady=5)

buttonMultiplayer = Button(
    left_frame, text="Multiplayer", command=on_button_multiplayer)
buttonMultiplayer.grid(row=2, column=0, padx=5, pady=5)

quit_button = Button(left_frame, text="Quit", command=quit_app)
quit_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
