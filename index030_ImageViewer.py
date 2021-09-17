"""
Cours : Build An Image Viewer App
Lien : https://www.youtube.com/watch?v=6zkOrq9YVik

Complément du cours précédent sur la boîte de dialogue :
Insertion de photos dans la fenêtre principale

Editeur : Laurent REYNAUD
Date : 17-09-21
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap # pour les photos
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index030_ImageViewer.UI', self)
        
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
            "C:/Users/LRCOM/pythonProjects/codemy_pyqt5/images",
            "Images (*.png);;Tous fichiers (*)")
        
        # Ouverture d'une photo
        self.pixmap = QPixmap(fname[0])
        
        # Ajout de la photo dans le widget
        self.label.setPixmap(self.pixmap)
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()