from tkinter import *
from PIL import Image, ImageTk #Non Nécéssaire (non utilisé)
from joueur import Joueur
from case import Case 
from personnage import Personnage
from question import Question
from plateau import Plateau
from tkinter import messagebox #Import pour la fenetre de vérification
from jeu import Jeu

# Interface du Menu
root = Tk()  # create root window
root.title("Qui-est-ce ?")
root.iconbitmap("QEC_Logo.ico")
root.config(bg="dodgerblue")

# Create Frame widget
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=0, column=0, padx=10, pady=5)

# Create frame within left_frame
tool_bar = Frame(left_frame, width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)

# Load logo
image = PhotoImage(file="Images_Personnages/QEC_Logo.png")
original_image = image.subsample(3, 3)  # resize image
Label(left_frame, image=original_image).grid(row=0, column=0, padx=5, pady=5)

# Function to open a new window with a message for solo


imagesfinales = []
image_cachee = None

def on_button_solo():
    new_window = Toplevel(root)
    new_window.title("Solo")
    new_window.geometry("700x600")  # resize window
    new_window.iconbitmap("QEC_Logo.ico")

    # Load logo
    logo = PhotoImage(file="Images_Personnages/QEC_Logo.png")
    new_window.logo = logo  # Keep a reference to avoid garbage collection
    logo_label = Label(new_window, image=logo)
    logo_label.pack(pady=10)
    Label(new_window, text="Choose your difficulty").pack(padx=20, pady=20)

    # Add new buttons to the new window
    buttonEasy = Button(new_window, text="Easy", command=lambda: open_easy_window(new_window))
    buttonEasy.pack(pady=10)
    buttonMedium = Button(new_window, text="Medium", command=not_available)
    buttonMedium.pack(pady=10)
    buttonHard = Button(new_window, text="Hard", command=not_available)
    buttonHard.pack(pady=10)

def toggle_case(event):
    button = event.widget
    if button["bg"] == "SystemButtonFace":
        button["bg"] = "dodgerblue"
    else:
        button["bg"] = "SystemButtonFace"

jeu = Jeu(1, Joueur("Joueur1",631565,"Basil"), Joueur("Joueur2",631565,"Basil"))
jeu.start() #On lance le jeu

images = ['Basil','Bill','Brian','Edna','Gary','Hannah','Ian','Isla','Jennifer','Joshua','Kelly','Kim','Maggie','Martine','Melvin','Mo','Natalie','Pete','Roy','Rupert','Simone','Stephen','Susan','XiaoMei']
cache = {}
# Initialisation du cache pour chaque image
for i in range(len(images)):
    cache[i] = False


def on_image_click(button, index_image):
    global imagesfinales, image_cachee

    print("Test clic : ", index_image)
    print(cache)

    # On vérifie si l'image est déjà cachée
    if index_image in cache and cache[index_image]:
        # Réaffiche l'image originale
        button.config(image=imagesfinales[index_image], bg='SystemButtonFace', text="")
        cache[index_image] = False
        jeu.persos[images[index_image].lower()].cache = False

    else:
        # Cache l'image et affiche un label avec le nom
        button.config(image=image_cachee, bg='grey', fg='black', text=images[index_image])
        cache[index_image] = True
        jeu.persos[images[index_image].lower()].cache = True
    




def open_easy_window(parent_window):

    global imagesfinales, image_cachee

    # Fermer la fenêtre parente
    parent_window.destroy()
    easy_window = Toplevel(root)
    easy_window.iconbitmap("QEC_Logo.ico")
    easy_window.title("Solo-Easy")

    # Ajouter le bouton "Quit" en haut à gauche
    quit_button = Button(easy_window, text="Quit", command=easy_window.destroy)
    quit_button.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    cases_frame = Frame(easy_window, bg="dodgerblue")
    cases_frame.grid(row=1, column=0, padx=10, pady=10)

    # Charger les images dans une liste
    
    for i in range(24):
        image = PhotoImage(file=f'Images_Personnages/{images[i]}.png')
        imagesfinales.append(image)

    # Charger l'image de fond (cachée)
    image_cachee = PhotoImage(file="Images_Personnages/bck_b_t.png")

    # Créer les boutons en utilisant les images
    for i in range(4):  # 4 lignes
        for j in range(6):  # 6 colonnes
            index = i * 6 + j
            button = Button(cases_frame, image=imagesfinales[index])
            # Utilisez une lambda pour capturer correctement la référence du bouton et de l'index
            button.config(command=lambda btn=button, idx=index: on_image_click(btn, idx))
            button.grid(row=i, column=j)

    # Ajouter une commande pour fermer la fenêtre "easy_window" et réafficher "root"
    easy_window.protocol("WM_DELETE_WINDOW", lambda: (
        easy_window.destroy(), root.deiconify()))
    easy_window.mainloop()

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