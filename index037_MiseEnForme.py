"""
Cours #37 : Hover and Focus Effects For Forms and Buttons
Lien : https://www.youtube.com/watch?v=wWqu6tKRM7I

Dans ce programme on intervient dans la mise en forme des widgets
à partir de l'application designer, en recourant aux instructions
qui sont utilisées dans le langage CSS

Pour une mise en forme des widgets dans l'application designer :
-> Clique droit sur le widget
-> Sélectionner : "Modifier la feuille de style..."

Editeur : Laurent REYNAUD
Date : 
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLineEdit, QPushButton, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index037_MiseEnForme.UI', self)
        
        # Configuration des widgets
        self.linedit = self.findChild(QLineEdit, "lineEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()