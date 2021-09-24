"""
Cours : Build A Tic Tac Toe Game
Lien : https://www.youtube.com/watch?v=5yyD-dQojC4

Dans ce programme on apprend à créer le jeu du morpion
(idem que dans tkinter)

Editeur : Laurent REYNAUD
Date : 24-09-2021
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index031_TicTacToe.UI', self)
        
        # Compteur pour savoir qui doit jouer avec un départ = 0
        self.counter = 0
        
        # Configuration des widgets
        "TODO: à compléter"
        self.label = self.findChild(QLabel, "label")
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        
        # Action d'exécuction sur les boutons
        self.button1.clicked.connect(lambda:self.clicker(self.button1))
        self.button2.clicked.connect(lambda:self.clicker(self.button2))
        self.button3.clicked.connect(lambda:self.clicker(self.button3))
        self.button4.clicked.connect(lambda:self.clicker(self.button4))
        self.button5.clicked.connect(lambda:self.clicker(self.button5))
        self.button6.clicked.connect(lambda:self.clicker(self.button6))
        self.button7.clicked.connect(lambda:self.clicker(self.button7))
        self.button8.clicked.connect(lambda:self.clicker(self.button8))
        self.button9.clicked.connect(lambda:self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def clicker(self, b):
        "Action selon le bouton appuyé"
        
        # Si le compteur est un chiffre pair
        if self.counter % 2 == 0:
            mark = 'X'
            self.label.setText("Au tour du 'O' à jouer ;)")
        else:
            mark = 'O'
            self.label.setText("Au tour du 'X' à jouer ;)")
        
        # Affichage du 'X' ou du 'O' lorsqu'on appuye sur le bouton
        b.setText(mark)
        # 'X' verrouillé
        b.setEnabled(False)
        
        # Incrémentation du compteur
        self.counter += 1
        
    def reset(self):
        "Relance du jeu"
        
         # Assignation d'une liste des boutons 1 à 9
        button_list = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9]
        
        for b in button_list:
            # Réinitialisation des boutons
            b.setText('')
            # Déverrouillage des boutons
            b.setEnabled(True)
        
        # Réinitialisation du texte    
        self.label.setText("X commence en premier !")
        
        # Réinitialisation du compteur
        self.counter = 0
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()