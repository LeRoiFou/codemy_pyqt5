"""
Cours : Bind Text Box Text To Label
Lien : https://www.youtube.com/watch?v=t7JZo2xbb8I

Dans ce programme on apprend à afficher dans l'etiquette
la saisie faite dans la zone de texte 
(voir tkinter index205_ZoneTexteBind)

Editeur : Laurent REYNAUD
Date : 13-01-22
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QLineEdit, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index044_TextBoxBind.UI', self)
        
        # Configuration des widgets
        self.label = self.findChild(QLabel, "label")
        self.edit = self.findChild(QLineEdit, "lineEdit")
        
        # Instruction pour copier le texte après avoir appuyé sur ENTREE
        self.edit.editingFinished.connect(self.hitEnter)
        
        # Instruction pour copier le texte dès la saisie
        self.edit.textChanged.connect(self.changeText)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def hitEnter(self):
        "Modification du texte après avoir appuyé sur ENTREE"
        self.label.setText(self.edit.text())
        
    def changeText(self):
        "Modification du texte dès la saisie"
        self.label.setText(self.edit.text())
        
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