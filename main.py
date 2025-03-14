
from tkinter import *
from PIL import Image, ImageTk #Non Nécéssaire (non utilisé)
from joueur import Joueur
from case import Case 
from personnage import Personnage
from question import Question
from plateau import Plateau
from tkinter import messagebox #Import pour la fenetre de vérification

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


images = ['Basil','Bill','Brian','Edna','Gary','Hannah','Ian','Isla','Jennifer','Joshua','Kelly','Kim','Maggie','Martine','Melvin','Mo','Natalie','Pete','Roy','Rupert','Simone','Stephen','Susan','XiaoMei']
cache = {}
# Initialisation du cache pour chaque image
for i in range(len(images)):
    cache[i] = False


def on_image_click(cases_frame, index_image):
    print("Test clic : ", index_image)
    print(cache)
    # print("Test, clique sur l'image ", index_image)
    # messagebox.showinfo("Information", "Button clicked!")

    # On check si l'image est déjà cachée
    if index_image in cache and cache[index_image]:
        button.config(image=PhotoImage(file=f'Images_Personnages/{images[index_image]}.png'), command=lambda button=button,
                      index=index_image: on_image_click(button, index_image))
        cache[index_image] = False
        
    else:
        
        button = Button(cases_frame, PhotoImage(file='Images_Personnages/bck_b_t.png'))
        button.config(command=lambda cases_frame=cases_frame,
                      index=index: on_image_click(cases_frame, index))
        button.grid(row=0, column=0)
        

        # button.config(image=PhotoImage(file='Images_Personnages/bck_b_t.png'), command=lambda button=button,
        #               index=index_image: on_image_click(button, index_image))
        label = Label(button, text=images[index_image], bg='grey', fg='black')
        label.place(relx=0.5, rely=0.5, anchor='center')
        cache[index_image] = True




def open_easy_window(parent_window):
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
    imagesfinales = []
    # image list line 63
    for i in range(24):
        # Remplacez 'image_{i}.gif' par le chemin de vos images
        image = PhotoImage(file=f'Images_Personnages/{images[i]}.png')
        imagesfinales.append(image)
    for i in range(4):  # 4 lignes
        for j in range(6):  # 6 colonnes
            index = i * 6 + j
            button = Button(cases_frame, image=imagesfinales[index])
            button.config(command=lambda cases_frame=cases_frame,
                          index=index: on_image_click(cases_frame, index))
            button.grid(row=i, column=j)

    # Ajouter une commande pour fermer la fenêtre "easy_window" et réafficher "root"
    easy_window.protocol("WM_DELETE_WINDOW", lambda: (
        easy_window.destroy(), root.deiconify()))
    easy_window.mainloop()
    # for i in range(4):
    #     for j in range(6):
    #         case_button = Button(cases_frame, text=f"Case {i*6 + j + 1}", width=10, height=5)
    #         case_button.grid(row=i, column=j, padx=5, pady=5)
    #         case_button.bind("<Button-1>", toggle_case)
 

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
