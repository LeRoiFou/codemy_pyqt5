"""
Cours #36 : Multiple Windows Inside Your App
Lien : https://www.youtube.com/watch?v=CvWl-Rhy2wI

Dans ce programme on a recours au widget MDI Area qui va être utilisé
en tant que 'cadre' pour ajouter des widgets à l'intérieur de ce widget

À titre d'exemple on apprend ici à ajouter autant de 
sous-fenêtres qu'on le souhaite dans le widget MDI Area

Editeur : Laurent REYNAUD
Date : 12-11-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QMdiArea, QLabel, QMdiArea, QMdiSubWindow, QPushButton, \
        QDesktopWidget, QTextEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index036_MultipleWindows.UI', self)
        
        # Configuration des widgets
        
        self.mdi = self.findChild(QMdiArea, 'mdiArea')
        self.label = self.findChild(QLabel, "label")
        self.button = self.findChild(QPushButton, "pushButton")
        
        # Bouton d'execution
        self.button.clicked.connect(self.add_window)
        
        # Assignation d'une variable en tant que compteur
        self.count = 0
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def add_window(self):
        ""
        
        # Incrémentation
        self.count = self.count + 1
        
        # Configuration d'une sous-fenêtre
        sub = QMdiSubWindow()
        
        # Ajout de la fenêtre :
        # c'est la page blanche qui est située 
        # en dessous de la barre de titres
        sub.setWidget(QTextEdit())
        
        # Configuration de la barre de titre
        sub.setWindowTitle("Fenêtre n° " + str(self.count))
        
        # Ajout des sous-fenêtres dans le widget MDI 
        self.mdi.addSubWindow(sub)
        
        # Affichage de la nouvelle sous-fenêtre
        sub.show()
        
        "Diverses fonctionnalités avec les sous-fenêtres :"
        
        # Affichage de la sous-fenêtre dans tout le cadre 
        # du widget MDIArea
        # self.mdi.tileSubWindows()
        
        # Affichage des sous-fenêtres en cascade
        self.mdi.cascadeSubWindows()
        
        # Autres fonctionnalités (pas très utiles...)
        # self.mdi.closeActiveSubWindow()
        # self.mdi.removeSubWindow()
        # self.mdi.subWindowList()
        
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()