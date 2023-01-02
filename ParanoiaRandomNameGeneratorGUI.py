#import sys
#sys.path.append('C:\\Users\\q_jun\\AppData\\Roaming\\Python\\Python310\\site-packages\\customtkinter')
from tkinter import *
# TKinter "modern look" library: https://github.com/TomSchimansky/CustomTkinter
# import customtkinter
import random

# To Do:
# - switch from PyQt to TKinter/customtkinter
# - gender selection Paranoia

import logging

# Might want to change filemode back to "w" when debugging -
# Having it set to "a" appends new log entries to the same file
# which could be handy for users trying to find generated names 
logging.basicConfig(
    level=logging.INFO,
    filename="RNG.log",
    filemode="a",
    format="%(asctime)s: %(levelname)s - %(message)s"
)


# Basic setup
root = Tk()

# Available name parts
first_names_f = ["Cor-A", "Bett-Y", "Dar-A", "Bann-I", "Ver-A", "Ver-O", "Chlo-E", "Hosh-I", "Stin-E", "Petr-A", "Laur-A", "Fatim-A", "Aysh-E", "Frey-A", "Lydi-A", "Gin-A", 
    "Gret-L", "Zo-E", "Zor-A", "Nadi-A", "The-A", "Chihir-O", "Han-A", "Hir-O", "Katan-A", "Ing-A", "Mar-I", "Alb-A", "Clar-A", "Dor-O", "Sierr-A", "Iri-S", "Kar-N", 
    "Lex-I", "Lilli-T", "Marg-A", "Marg-O", "Per-I", "Titani-A", "Urs-A", "Ursul-A", "Anik-A", "Amel-I", "Beck-Y", "Nel-E", "Ima-N", "Ki-A", "Mbal-I", "Ut-E", "Fel-O",
    "Natash-A", "Samir-A", "Mir-I", "Emm-A", "Ell-A", "Ezr-A", "Trud-E", "Isol-D", "Rut-H", "Nal-A", "Alin-A", "Male-A", "Vaness-A", "Chiar-A", "Pi-A", "Misch-L", "Schanta-L",
    "Caro-L", "Grac-E", "Rile-Y", "Dört-E", "Ma-I"]
first_names_m = ["Hug-O", "Core-E", "Stefa-N", "Bret-T", "Juli-O", "Han-S", "Rüdig-R", "Lui-S", "Lar-S", "Maik-L", "Björ-N", "Tho-R", "Marti-N", "Jerr-Y", "Frit-Z", 
    "Hassa-N", "Al-I", "Core-Y", "Sandr-O", "Dimitr-I", "Serge-Y", "Gok-U", "Hide-O", "Ju-N", "Take-O", "Ri-O", "Artur-O", "Cesa-R", "Ch-E", "Edd-I", "Leo-N", "Ramo-N",
    "Vit-O", "Adoni-S", "Jure-K", "Kost-A", "Owe-N", "Ti-M", "Abdu-L", "Ama-L", "Cayma-N", "Elo-N", "Fabi-O", "Habib-I", "Jojo-J", "Kof-I", "Mahd-I", "Kur-T", "Peterche-N",
    "Hors-T", "Nelso-N", "Ne-O", "Sai-D", "Sami-R", "Ott-O", "Jaco-B", "Diet-R", "Jürg-N", "Bertra-M", "Kaspa-R", "Jaspe-R", "Tilma-N", "Tobia-S", "Torsten-D", "Hold-N",
    "Rafa-L", "Arvi-D", "Samu-L", "Malt-E", "Andr-U", "Rog-R"]
first_names_n = ["Roc-K", "Fli-P", "Morg-N", "Jord-N", "Vi-C", "Al-X", "Blak-E", "Fritz-I", "Ka-I", "Max-I", "Sa-M", "Ja-Y", "Hunt-R", "Charl-E", "Sim-P", "Vany-A", 
    "Do-I", "Ky-O", "Cru-Z", "Tro-Y", "Did-I", "Noname-0", "Robi-N"]

fantasy_parts = ["gro", "ka", "ron", "ra", "bis", "cal", "o", "ben", "sa", "gor", "lis", "tor", "i", "ni", "na", "bos", "chi", "sam", "son", "nu", "gel", "ei", "vel", "wen",
    "ter", "jan", "ha", "fu", "q'", "la", "'", "y", "da", "bäm", "le", "li", "sch", "as", "a", "an", "le", "os", "te", "ta", "tar"]

sector_code_home = "NNG"
sector_code = ["HYT", "OOT", "FCK", "EDN", "PER", "GER", "LOL", "XOR", "BRB", "AFK", "KEK", "404", "XXL", "SPD", "ERR", "WAT", "HMM", "WTF", "BOS", "EXT", "OHO", "NYC"]

def generate_fantasy():
    max = len(fantasy_parts) - 1
    name_parts = random.randint(2,5)
    name = ""
    while name_parts > 0:
        name_parts = name_parts - 1
        pick = random.randint(0, max)
        name = name + fantasy_parts[pick]
        logging.debug("Fantasy name part %s generated", name)
    result_label["text"] = name.capitalize()
    logging.debug("Fantasy name %s passed to result label", name)
    logging.info("Fantasy name %s generated", name.capitalize())
    return name
    
def generate_first_name_rnd():
    gender_nr = random.randint(1,3)
    match gender_nr:
        case 1:
            max = len(first_names_m) - 1
            pick = random.randint(0, max)
            logging.debug("Random gender name %s picked", first_names_m[pick])
            return first_names_m[pick]
        case 2:
            max = len(first_names_f) - 1
            pick = random.randint(0, max)
            logging.debug("Random gender name %s picked", first_names_f[pick])
            return first_names_f[pick]
        case 3:
            max = len(first_names_n) - 1
            pick = random.randint(0, max)
            logging.debug("Random gender name %s picked", first_names_n[pick])
            return first_names_n[pick]

def generate_sector_name():
    max = len(sector_code) - 1
    logging.debug("Sector names available: %s", str(max))
    pick = random.randint(1, max)
    logging.debug("Sector %s chosen, name %s generated", str(pick), sector_code[pick])
    return sector_code[pick]

def generate_clone_number():
    rcn = random.randint(1, 6)
    logging.debug("Clone number generated: %s", str(rcn))
    return str(rcn)

def count_first_names():
    logging.debug(
        "Female first names: %s\nMale first names: %s\nEnby first names: %s",
        str(len(first_names_f)), str(len(first_names_m)), str(len(first_names_n))
    )

# GUI functions
def button_generate_func(radio_status):
    if radio_status == 1: # Fantasy
        logging.debug("Radio button 'fantasy' clicked")
        generate_fantasy()
    elif radio_status == 2: # Paranoia RPG
        logging.debug("Radio button 'paranoia' clicked")
        result_label["text"] = generate_first_name_rnd() + "-" + generate_sector_name().upper() + "-" + generate_clone_number()
        logging.debug("Paranoia name %s passed to result label", result_label["text"])
        logging.info("Paranoia name %s generated", result_label["text"])
    else:
        logging.error("Undefined radio button clicked")

## Text for Labels (and other elements) ##
root.title("Random Name Generator")
intro_text = "Welcome to the Random Name Generator."
middle_text = "Choose a theme."
frb_text = "Fantasy           " # I feel deeply ashamed. Will sure fix this later ...
prb_text = "Paranoia RPG"
button_text = "Generate name!"
result_text = "Click generate name \nto get started!"

## Window Size, Position, Layout ##
bg_color = '#c0d6e4'
width, height = 300, 300
screen_w, screen_h = root.winfo_screenwidth(), root.winfo_screenheight()
winpos_x, winpos_y = int(screen_w/2 - width/2), int(screen_h/2 - height/2)

root.geometry(f'{width}x{height}+{winpos_x}+{winpos_y}') # make sure the window is centered on user's screen
root.configure(bg=bg_color)
root.resizable(False, False)
# Add Icon
# Colors

## Creating labels and buttons (and the window) ##
intro_label = Label(root, text=intro_text, font=('Helvetica bold', 10), background=bg_color)

middle_label = Label(root, text=middle_text, font=('Helvetica bold', 10), pady=5, background=bg_color)
buffer_label_1 = Label(root, text="", pady=5, background=bg_color)
buffer_label_2 = Label(root, text="", pady=5, background=bg_color)
button_generate = Button(root, text=button_text, font=('Helvetica bold', 10), padx=10, pady=8, command=lambda: button_generate_func(rbval.get()), background="#63D471", fg="#5E4B56")
result_label = Label(root, text=result_text, pady=10, font=('Helvetica bold', 16), width=40, background='#468499')
#result_textfield = Text(root, height=2, width=10)
rbval = IntVar()
rbval.set("1")

radio_fantasy = Radiobutton(root, text=frb_text, variable=rbval, value=1, command=rbval.get(), width=10, background=bg_color)
radio_paranoia = Radiobutton(root, text=prb_text, variable=rbval, value=2, command=rbval.get(), width=10, background=bg_color)

## Putting stuff on screen ##
# Could do all this in one line - but readability would suck:
# intro_label = Label(root, text="Welcome to the Random Name Generator.\nChoose a theme.").grid(row=0, column=0)
# stick="W"
root.grid_columnconfigure(0, weight=1) # This centers the widgets of the grid in parent window
intro_label.grid(row=0, column=0)
middle_label.grid(row=1, column=0)
radio_fantasy.grid(row=2, column=0)
radio_paranoia.grid(row=3, column=0)
buffer_label_1.grid(row=4, column=0)
button_generate.grid(row=5, column=0)
buffer_label_2.grid(row=6, column=0)
result_label.grid(row=7, column=0)
#result_textfield.grid(row=6, column=0)
#result_textfield.insert('end', update_text_field()) # Doesn't update yet

global sector_generated
global clone_nr_generated
sector_generated = generate_sector_name()
clone_nr_generated = str(generate_clone_number())

root.mainloop()