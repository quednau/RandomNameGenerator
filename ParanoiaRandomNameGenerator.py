import random
import time
# Necessary imports for GUI/PyQt:
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Paranoia names follow this pattern:
# {first name-some letter}-{3-character-sector-code}-{clone number}

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

sector_code_home = "NNG"
sector_code = ["HYT", "OOT", "FCK", "EDN", "PER", "GER", "LOL", "XOR", "BRB", "AFK", "KEK", "404", "XXL", "SPD", "ERR", "WAT", "HMM", "WTF", "BOS", "EXT", "OHO", "NYC"]

def initial_input():
    print("What kind of name to generate?")
    gender_input = input("(M)ale, (F)emale, e(N)by? [Press (X) to e(X)it]")
    return gender_input

def generate_first_name(user_input):
    match user_input:
        case "m":
            max = len(first_names_m) - 1
            pick = random.randint(0, max)
            return first_names_m[pick]
        case "f":
            max = len(first_names_f) - 1
            pick = random.randint(0, max)
            return first_names_f[pick]
        case "n":
            max = len(first_names_n) - 1
            pick = random.randint(0, max)
            return first_names_n[pick]
        case "c":
            count_first_names()
            input("Press any key to close.")
            quit()
        case "x":
            print("Thank you for using this program. Exiting ...")
            time.sleep(2)
            quit()
        case _: 
            return "[Error: Gender not found.]"

def generate_sector_name():
    max = len(sector_code) - 1
    pick = random.randint(1, max)
    return sector_code[pick]

def generate_clone_number():
    rcn = random.randint(1, 6)
    return str(rcn)

def end_program():
    input("Press enter to continue.")

def count_first_names():
    print("Female first names: " + str(len(first_names_f)))
    print("Male first names: " + str(len(first_names_m)))
    print("Enby first names: " + str(len(first_names_n)))

# main routine

#count_first_names()
#print(generate_first_name(initial_input()) + "-" + generate_sector_name() + "-" + generate_clone_number())

while True:
    print(f'{generate_first_name(initial_input())}-{generate_sector_name()}-{generate_clone_number()}')
    end_program()