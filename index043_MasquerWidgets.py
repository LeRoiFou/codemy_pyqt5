"""
Cours #43 : How To Hide or Show Widgets From GUI
Lien : https://www.youtube.com/watch?v=LCJEyuCZlAY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=43

Dans ce programme on apprend à masquer et à réafficher un widget

Editeur : Laurent REYNAUD
Date : 07-01-22
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLineEdit, QPushButton, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index043_MasquerWidgets.UI', self)
        
        # Configuration des widgets
        self.edit = self.findChild(QLineEdit, "lineEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        
        # Méthode rattachée au bouton d'exécution
        self.button.clicked.connect(self.hide_unhide)
        
        # Assignation de l'affichage ou non de la zone de saisie
        self.hidden = False
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def hide_unhide(self):
        "Méthode pour masquer / afficher la zone de saisie"
        
        if self.hidden: # Si vrai
            self.edit.show()
            self.hidden = False
        else:
            self.edit.hide()
            self.hidden = True
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()