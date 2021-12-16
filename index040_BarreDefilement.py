"""
Cours : Horizontal Sliders - PyQt5 GUI Thursdays #40
Lien : https://www.youtube.com/watch?v=lQ4KVj-EVOk


Editeur : Laurent REYNAUD
Date : 16-12-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QSlider, QDesktopWidget
from PyQt5 import uic
from PyQt5 import QtCore # Centrage du texte
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index040_BarreDefilement.UI', self)
        
        # Configuration des widgets
        self.label = self.findChild(QLabel, "label")
        self.slider = self.findChild(QSlider, "horizontalSlider")
        
        # Centrage du texte
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        
        # Propriétés de la barre de défilement
        self.slider.setMinimum(10) # minimum
        self.slider.setMaximum(90) # maximum
        self.slider.setValue(20) # position
        # self.slider.setTickPosition(QSlider.TicksBelow) # réf en dessous la barre
        self.slider.setTickPosition(QSlider.TicksAbove) # réf au-dessus de la barre
        self.slider.setTickInterval(20)
        self.slider.setSingleStep(5) # saut d'intervalle avec la souris
        
        # Déplacement de la barre de défilement
        self.slider.valueChanged.connect(self.slide_it)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def slide_it(self, value):
        "Modif du texte en déplaçant le bouton de la barre de défilement"
        
        self.label.setText(str(value))
    
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