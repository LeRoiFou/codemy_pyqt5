"""
Cours : Create An LCD Clock - PyQt5 GUI Thursdays #35
Lien : https://www.youtube.com/watch?v=CcnsV4qlBGQ

Dans ce programme on a recours au widget LCD Number dans Designer
(partie Display Widget) pour afficher une horloge

Pour changer la couleur de fond du widget, clique droit sur le widget
dans Designer puis sélectionner 'Modifier la feuille de style' puis
voir saisies faites

Editeur : Laurent REYNAUD
Date : 04-11-2021
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLCDNumber, QDesktopWidget
from PyQt5 import uic
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime

import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index035_LCDClock.UI', self)
        
        # Configuration des widgets
        self.lcd = self.findChild(QLCDNumber, "lcdNumber")
        
        # Assignation d'un temps
        self.timer = QTimer()
        self.timer.timeout.connect(self.lcd_number)
        
        # Début du compteur et mise à jour par seconde
        self.timer.start(1_000)
        
        # Appel de la méthode lcd_number()
        self.lcd_number()
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def lcd_number(self):
        
        # Configuration du temps
        time = datetime.now() # Temps actuel
        formatted_time = time.strftime('%H:%M:%S') # Format du temps
        
        # Police d'écriture
        self.lcd.setDigitCount(8) # Taille de la police d'écriture
        self.lcd.setSegmentStyle(QLCDNumber.Flat) # Ecriture en noire
        
        # Affichage du temps
        self.lcd.display(formatted_time) 
        
        
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