"""
Cours : 
Add Text To Images With Pillow - PyQt5 GUI Thursdays #41
Lien : https://www.youtube.com/watch?v=0uefpn7Xcj8

Dans ce programme on apprend à insérer du texte dans une image
L'image est chargée dans le widget Label partie QLabel -> pixmap
(Voir cours tkinter index203_TextesDansImages)

Editeur : Laurent REYNAUD
Date : 31-12-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QLineEdit, QPushButton, QDesktopWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap #affichage de l'image modifiée
import sys
from PIL import Image, ImageFont, ImageDraw #module Pillow

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index042_TexteDansImage.UI', self)
        
        # Configuration des widgets
        self.label = self.findChild(QLabel, "label")
        self.edit = self.findChild(QLineEdit, "lineEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        
        # Méthode rattachée au bouton d'exécution
        self.button.clicked.connect(self.addText)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def addText(self):
        "Ajout du texte à l'image"
        
        # Récupération du texte saisi
        myText= self.edit.text()
        
        # Chargement de l'image
        myImage = Image.open('images/Toblerone.png')
        
        # Formatage du texte inséré dans l'image
        textFont = ImageFont.truetype('arial.ttf', 46)
        
        # Affichage de l'image
        editImage = ImageDraw.Draw(myImage)
        
        # Positionnement du texte inséré dans l'image 
        # et formatage de l'image
        editImage.text((128,320), myText, ('red'), font=textFont)
        
        # Sauvegarde de l'image modifiée
        myImage.save('images/Toblerone2.png')
        
        # Mise à jour de l'image
        pixmap = QPixmap('images/Toblerone2.png')
        self.label.setPixmap(pixmap)
        
        # Réinitialisation du texte saisie
        self.edit.setText('')
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()