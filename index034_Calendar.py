"""
Cours : How To Use The Calendar Widget
Lien : https://www.youtube.com/watch?v=dx_5UvjAJVQ

Dans ce programme on a recours au widget 'Calendar Widget' présent
dans l'application Designer (partie Display Widgets)

Editeur : Laurent REYNAUD
Date : 30-10-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QCalendarWidget, QLabel, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index034_Calendar.UI', self)
        
        # Configuration des widgets
        self.calendar = self.findChild(QCalendarWidget, 'calendarWidget')
        self.label = self.findChild(QLabel, "label")
        
        # Recours à la méthode ci-dessous
        self.calendar.selectionChanged.connect(self.grab_date)

        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def grab_date(self):
        "Sélection d'une date"
        
        # Sélection d'une date
        dateSelected = self.calendar.selectedDate()
    
        
        # Affichage de la date format AAAA-MM-JJ
        # self.label.setText(str(dateSelected.toPyDate()))
        
        # Affichage de la date format anglais (bof...)
        self.label.setText(str(dateSelected.toString()))
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()