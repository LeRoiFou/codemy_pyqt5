"""
Cours : Build A Tic Tac Toe Game
Lien : https://www.youtube.com/watch?v=RB8CgQ1XToA

Dans ce programme on apprend à créer le jeu du morpion
(idem que dans tkinter)

Editeur : Laurent REYNAUD
Date : 01-10-2021
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index032_TicTacToe.UI', self)
        
        # Compteur pour savoir qui doit jouer avec un départ = 0
        self.counter = 0
        
        # Configuration des widgets
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
        
        # Vérifier si le joueur a gagné
        self.checkWin()
              
    def checkWin(self):
        "Vérification si un joueur a gagné"
        
        # La 1ère ligne
        if (self.button1.text() != '' 
            and 
            self.button1.text() == self.button4.text()
            and
            self.button1.text() == self.button7.text()):
            self.win(self.button1, self.button4, self.button7)
        
        # La 2nde ligne
        if (self.button2.text() != '' 
            and 
            self.button2.text() == self.button5.text()
            and
            self.button2.text() == self.button8.text()):
            self.win(self.button2, self.button5, self.button8)
            
        # La 3ème ligne
        if (self.button3.text() != '' 
            and 
            self.button3.text() == self.button6.text()
            and
            self.button3.text() == self.button9.text()):
            self.win(self.button3, self.button6, self.button9)
            
        # La 1ère colonne
        if (self.button1.text() != '' 
            and 
            self.button1.text() == self.button2.text()
            and
            self.button1.text() == self.button3.text()):
            self.win(self.button1, self.button2, self.button3)
            
        # La 2nde colonne
        if (self.button4.text() != '' 
            and 
            self.button4.text() == self.button5.text()
            and
            self.button4.text() == self.button6.text()):
            self.win(self.button4, self.button5, self.button6)
        
        # La 3ème colonne
        if (self.button7.text() != '' 
            and 
            self.button7.text() == self.button8.text()
            and
            self.button7.text() == self.button9.text()):
            self.win(self.button7, self.button8, self.button9)
            
        # La diagonale bas gauche haut droite
        if (self.button3.text() != '' 
            and 
            self.button3.text() == self.button5.text()
            and
            self.button3.text() == self.button7.text()):
            self.win(self.button3, self.button5, self.button7)
            
        # La diagonale haut gauche bas droite
        if (self.button1.text() != '' 
            and 
            self.button1.text() == self.button5.text()
            and
            self.button1.text() == self.button9.text()):
            self.win(self.button1, self.button5, self.button9)
        
    def win(self, a, b, c):
        "Résultat de celui qui a gagné"
        
        # Changement de la couleur des 'X' / 'O'
        a.setStyleSheet('QPushButton {color : red;}')
        b.setStyleSheet('QPushButton {color : red;}')
        c.setStyleSheet('QPushButton {color : red;}')
        
        # Modification du texte
        self.label.setText(f"{a.text()} a gagné !")
        
        # Verrouillage du jeu
        self.disable()
        
    def disable(self):
        "Verrouillage du jeu"
        
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
            # Verrouillage des boutons
            b.setEnabled(False)
 
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
            # Réinitialisation de la couleur des boutons
            b.setStyleSheet('QPushButton {color : #797979;}')
        
        # Réinitialisation du texte    
        self.label.setText("X commence en premier !")
        
        # Réinitialisation du compteur
        self.counter = 0
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()