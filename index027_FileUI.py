"""
Cours : How To Load PYQT5 Designer UI File
Lien : https://www.youtube.com/watch?v=p6Q2-m9i4Fg

Dans ce programme on apprend à intervenir sur le fichier .ui
sans générer à nouveau un fichier de l'application Designer et
permettant ainsi de commettre des erreurs en copiant/collant

Saisies manuelles ci-dessous pour charger l'application généré du fichier .ui

Editeur : Laurent REYNAUD
Date : 26-08-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index027_FileUI.ui', self)
        
        # Configuration des widgets
        self.label = self.findChild(QLabel, "label")
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.clear_button = self.findChild(QPushButton, "pushButton_Delete")
        
        # Méthodes détaillées ci-après
        self.button.clicked.connect(self.clicker)
        self.clear_button.clicked.connect(self.clearer)
        
        # Affichage de l'application
        self.show()
        
    def clicker(self):
        "Modification du titre"
        
        self.label.setText(f"Salut {self.textedit.toPlainText()} !")
        self.textedit.clear()
        
    def clearer(self):
        "Effacement du texte"
        
        self.textedit.clear()
        self.label.setText("Entrer votre nom...")
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()