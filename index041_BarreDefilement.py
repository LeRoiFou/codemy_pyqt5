"""
Cours : Vertical Sliders - PyQt5 GUI Thursdays #41
Lien : https://www.youtube.com/watch?v=BvveykrtWg8

Suite du cours précédent : cette fois-ci on créé une barre
de défilement verticale

Editeur : Laurent REYNAUD
Date : 24-12-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QSlider, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index041_BarreDefilement.UI', self)
        
        # Configuration des widgets
        self.label = self.findChild(QLabel, "label")
        self.slider = self.findChild(QSlider, "verticalSlider")
        
        # Déplacement de la barre de défilement
        self.slider.valueChanged.connect(self.slide_it)
        
        # Configuration de la barre de défilement
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        self.slider.setValue(10) # position
        self.slider.setTickPosition(QSlider.TicksLeft) # position barre graduée
        # # self.slider.setTickPosition(QSlider.TicksRight) # position à droite
        # self.slider.setTickPosition(QSlider.TicksBothSides) # double position
        self.slider.setTickInterval(5) # écart graduation barre graduée
        self.slider.setSingleStep(5) # écart défilement
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def slide_it(self, value):
        
        # Modification du texte
        self.label.setText(str(value))
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
