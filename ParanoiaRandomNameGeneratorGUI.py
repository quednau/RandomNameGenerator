from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import random
# Note: After 1 painful hour of troubleshooting, I learned that PyQt-tools isn't supporting Python 3.10 yet ...
# Tutorial: https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
# Tutorial: https://www.guru99.com/pyqt-tutorial.html
# Tutorial-Video by Python Simplified Woman from Vancouver: https://www.youtube.com/watch?v=9iZLDnW_vwU

# To Do:
# - gender selection Paranoia

class WindowMaker(QWidget):
    def __init__(self): # Note: This NEEDS to exist
        super(WindowMaker, self).__init__()
        # Syntax: win.setGeometry(xpos, ypos, width, height)
        self.setGeometry(750, 250, 350, 300)
        self.setWindowTitle("RNG - Random Name Generator")
        self.setWindowIcon(QtGui.QIcon('bridge.png'))
        self.setStyleSheet("background: #ddccff;")
        self.initUI()

    def initUI(self):
        # Define upper label
        self.intro_label = QtWidgets.QLabel(self)
        self.intro_label.setText("Welcome to the Random Name Generator.\nChoose a theme.")
        self.intro_label.move(20, 100) # doesn't do anything b/c layout
        self.intro_label.setStyleSheet("margin-bottom: 10px;")
        self.intro_label.setAlignment(QtCore.Qt.AlignCenter)
        self.update_intro()

        #Define button(s)
        # create a layout for radio buttons first
        layout = QVBoxLayout()
        #layout = QGridLayout()
        self.setLayout(layout)

        rb_fantasy = QRadioButton('Fantasy', self)
        rb_fantasy.toggled.connect(self.update_radio)
        rb_fantasy.toggled.connect(self.fantasy_selected)
        rb_fantasy.setChecked(True)
        rb_fantasy.setStyleSheet("border: 2px hidden; margin-left: auto;")
        
        rb_paranoia = QRadioButton('Paranoia RPG', self)
        rb_paranoia.toggled.connect(self.update_radio)
        rb_paranoia.toggled.connect(self.paranoia_selected) # For debugging
        rb_paranoia.setStyleSheet("border: 2px hidden; margin-left: auto;")

        # Confirm button
        self.button_confirm = QtWidgets.QPushButton("Generate Name", self)
        self.button_confirm.setStyleSheet("margin-top: 10px; min-height: 40px;")
        # self.button_confirm.move(20, 160) # This doesn't do anything while in layout
        self.button_confirm.clicked.connect(self.button_confirm_pressed)
        self.button_confirm.clicked.connect(lambda: self.on_click(rb_paranoia.isChecked(), self.button_confirm))

        # Result label: Change to text field
        #self.result_label = QLabel('', self)
        self.result_label = QLineEdit(self)
        self.result_label.setStyleSheet("font-size: 20px;")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)

        # Just wanted to try adding an image, might delete later
        image = QPixmap("cardboard_meme.jpg")
        resized_image = image.scaled(280, 280)
        self.image_label = QLabel()
        self.image_label.setPixmap(resized_image)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter) # not really needed

        layout.addWidget(self.intro_label)
        layout.addWidget(self.image_label)
        layout.addWidget(rb_fantasy)
        layout.addWidget(rb_paranoia)
        layout.addWidget(self.button_confirm)
        layout.addWidget(self.result_label)
        

    def on_click(self, check, label):
        if check:
            if debug_mode == True: print("Paranoia")
            sector_generated = generate_sector_name()
            clone_nr_generated = str(generate_clone_number())
            name = generate_first_name_rnd() + "-" + sector_generated + "-" + clone_nr_generated
            self.result_label.setText(name)
            if debug_mode == True: print(name)
        else:
            name = generate_fantasy()
            self.result_label.setText(name.capitalize())
            if debug_mode == True: print(name)
    
    def button_confirm_pressed(self):
            #sector_generated = generate_sector_name()
            #self.result_label.setText(generate_paranoia(sector_generated))
            print("Button pressed")
            #self.update_intro()
        
    def update_intro(self):
        self.intro_label.adjustSize()

    def update_radio(self):
        # get the radio button the send the signal
        rb = self.sender()
        # Debug-check if the radio button is checked
        #if rb.isChecked():
            #self.result_label.setText(f'You selected {rb.text()}')

    def paranoia_selected(self, selected):
        if selected: print("Paranoia selected.")

    def fantasy_selected(self, selected):
        if selected: print("Fantasy selected.")


def window():
    app = QApplication(sys.argv)
    win = WindowMaker()
    # Actually show the window (and make sure that it exits on "x")
    win.show()
    sys.exit(app.exec_())

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
        if debug_mode == True: print(name)
    return name
    

#def generate_paranoia(sector):
    ## results = f'{generate_first_name("m"())}-{generate_sector_name()}-{generate_clone_number()}'
    #clone_nr_generated = str(generate_clone_number())
    #results = generate_first_name_rnd + "-" + sector + "-" + clone_nr_generated # generate_first_name("m") + "-" + str(generate_sector_name)
    #print(generate_sector_name)
    #print(str(generate_sector_name))
    #return results

def generate_first_name_rnd():
    gender_nr = random.randint(1,3)
    match gender_nr:
        case 1:
            max = len(first_names_m) - 1
            pick = random.randint(0, max)
            return first_names_m[pick]
        case 2:
            max = len(first_names_f) - 1
            pick = random.randint(0, max)
            return first_names_f[pick]
        case 3:
            max = len(first_names_n) - 1
            pick = random.randint(0, max)
            return first_names_n[pick]

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
            quit()
        case _: 
            return "[Error: Gender not found.]"

def generate_sector_name():
    max = len(sector_code) - 1
    max_str = str(max)
    if debug_mode == True: print("max: " + max_str)
    pick = random.randint(1, max)
    pick_str = str(pick)
    if debug_mode == True:
        print("pick: " + pick_str)
        print("pick as a string: " + sector_code[pick])
    return sector_code[pick]

def generate_clone_number():
    rcn = random.randint(1, 6)
    return str(rcn)

def count_first_names():
    print("Female first names: " + str(len(first_names_f)))
    print("Male first names: " + str(len(first_names_m)))
    print("Enby first names: " + str(len(first_names_n)))

# Execute!
global debug_mode
debug_mode = False

global sector_generated
global clone_nr_generated
sector_generated = generate_sector_name()
clone_nr_generated = str(generate_clone_number())
window()