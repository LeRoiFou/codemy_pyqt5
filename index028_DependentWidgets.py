"""
Cours : Dependent Comboboxes
Lien : https://www.youtube.com/watch?v=P6rJHEMQkfI

Dans ce programme on apprend à dépendre un menu déroulant à un autre menu
déroulant (similaire cours tkinter #152)

Editeur : Laurent REYNAUD
Date : 02-09-2021
"""

from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, \
    QDesktopWidget, QLabel
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index028_DependentWidgets.UI', self)
        
        # Configuration des widgets
        self.combo_left = self.findChild(QComboBox, "comboBox_Left")
        self.combo_right = self.findChild(QComboBox, "comboBox_Right")
        self.label = self.findChild(QLabel, "label")
        
        # Ajout des données aux combobox
        self.combo_left.addItem("Mâle", ['John', 'Wes', 'Dean'])
        self.combo_left.addItem("Femelle", ['Erin', 'Steph', 'Beth'])
        
        # Cliquer sur les menus déroulants
        self.combo_left.activated.connect(self.clicker)
        self.combo_right.activated.connect(self.clicker2)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def clicker(self, index):
        "Lien entre le menu déroulant de gauche avec celui de droite"
        
        # Réinitialisation du menu déroulant de droite
        self.combo_right.clear()
        
        # Faire la dépendance entre ces deux menus déroulants
        self.combo_right.addItems(self.combo_left.itemData(index))
        
    def clicker2(self):
        "Mise à jour du texte"
        
        self.label.setText(
            f"Tu as choisi : {self.combo_right.currentText()} - {self.combo_left.currentText()}")
        
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()