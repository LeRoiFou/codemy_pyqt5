"""
Cours : Change Background Color With Menu
Lien : https://www.youtube.com/watch?v=FgvZTJYITGg

Dans ce programme on apprend à changer la couleur de fond
de la fenêtre principale

Editeur : Laurent REYNAUD
Date : 07-10-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QMenu, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index033_BackgroundColor.UI', self)
        
        # Configuration des widgets
        # self.menu = self.findChild(QMenu, "menuCouleurs")
        
        # Déclenchement des couleurs
        self.actionNoir.triggered.connect(lambda:self.change('Black'))
        self.actionBlanc.triggered.connect(lambda:self.change('White'))
        self.actionRouge.triggered.connect(lambda:self.change('Red'))
        self.actionBleu.triggered.connect(lambda:self.change('Blue'))
        self.actionVert.triggered.connect(lambda:self.change('Green'))
        self.actionJaune.triggered.connect(lambda:self.change('Yellow'))
       
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def change(self, color):
        "Méthode pour déclencher la couleur"
        
        # Changement de la couleur de fond de la fenêtre principale
        self.setStyleSheet(f'background-color: {color};')
        
        # Changement du titre
        self.setWindowTitle(f"Tu as changé la couleur en {color}")
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()