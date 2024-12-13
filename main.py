from case import Case
from jeu import Jeu
from joueur import Joueur, Ordi
from personnage import Personnage
from plateau import Plateau
from question import Question
from tkinter import*

root = Tk()  # create root window
root.title("Qui-est-ce ?")
root.config(bg="dodgerblue")

# Set the window icon
#root.iconbitmap('path_to_icon.ico')

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
    # Load logo
    logo = PhotoImage(file="QEC_Logo.png")
    logo_label = Label(new_window, image=logo)
    logo_label.image = logo  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=10)
    Label(new_window, text="Choose your difficulty").pack(padx=20, pady=20)
    # Add new buttons to the new window
    buttonHard = Button(new_window, text="Hard")
    buttonHard.pack(pady=10)
    buttonMedium = Button(new_window, text="Medium")
    buttonMedium.pack(pady=10)
    buttonEasy = Button(new_window, text="Easy")
    buttonEasy.pack(pady=10)

# Function to close the window
def quit_app():
    root.quit()

# Function to open a new window with a message
def on_button_multiplayer():
    new_window = Toplevel(root)
    new_window.title("Multiplayer")
    Label(new_window, text="Multiplayer not available yet").pack(padx=20, pady=20)

# Create buttons and place them under the logo
buttonSolo = Button(left_frame, text="Solo", command=on_button_solo)
buttonSolo.grid(row=1, column=0, padx=5, pady=5)

buttonMultiplayer = Button(left_frame, text="Multiplayer", command=on_button_multiplayer)
buttonMultiplayer.grid(row=2, column=0, padx=5, pady=5)

quit_button = Button(left_frame, text="Quit", command=quit_app)
quit_button.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
