"""
Cours : File Dialog Boxes With QFileDialog
Lien : https://www.youtube.com/watch?v=gg5TepTc2Jg

Dans ce programme on apprend à ouvrir une boîte de dialogue

Editeur : Laurent REYNAUD
Date : 10-09-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index029_FileDialogBoxes.UI', self)
        
        # Configuration des widgets
        "TODO: à compléter"
        self.label = self.findChild(QLabel, "label")
        self.button = self.findChild(QPushButton, "pushButton")
        
        # Ouverture de la boîte de dialogue
        self.button.clicked.connect(self.clicker)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def clicker(self):
        "Ouverture de la boîte de dialogue"
        
        # Assignation d'une variable
        fname = QFileDialog.getOpenFileName(
            self, 
            "Ouvrir un fichier", 
            "C:/Users/LRCOM/pythonProjects/codemy_pyqt5",
            "Tous fichiers (*);;Fichiers Python (*.py)")
        
        # Affichage à l'écran chemin du fichier ouvert
        if fname:
            self.label.setText(fname[0])
        
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()