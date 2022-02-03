"""
Cours #47 : Build A Blackjack Card Game
Lien : https://www.youtube.com/watch?v=0SdF9sJXgUE

Jeu de cartes black jack

Editeur : Laurent REYNAUD
Date : 03-02-22
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap # Insertion des images
import sys
import random

class UI(QMainWindow):
    
    def __init__(self):
        super(UI, self).__init__()
        
        # Chargement du fichier ui
        uic.loadUi('index047_BlackJack.UI', self)
        
        # Configuration des widgets
        self.dealerTitle = self.findChild(QLabel, "dealerTitle")
        self.playerTitle = self.findChild(QLabel, "playerTitle")
        self.dealerCard1 = self.findChild(QLabel, "dealerCard1")
        self.dealerCard2 = self.findChild(QLabel, "dealerCard2")
        self.dealerCard3 = self.findChild(QLabel, "dealerCard3")
        self.dealerCard4 = self.findChild(QLabel, "dealerCard4")
        self.dealerCard5 = self.findChild(QLabel, "dealerCard5")
        self.playerCard1 = self.findChild(QLabel, "playerCard1")
        self.playerCard2 = self.findChild(QLabel, "playerCard2")
        self.playerCard3 = self.findChild(QLabel, "playerCard3")
        self.playerCard4 = self.findChild(QLabel, "playerCard4")
        self.playerCard5 = self.findChild(QLabel, "playerCard5")
        self.shuffleButton = self.findChild(QPushButton, "shuffleButton")
        self.hitMeButton = self.findChild(QPushButton, "hitMeButton")
        self.standButton = self.findChild(QPushButton, "standButton")
        
        # Dès le lancement du jeu, affichage au hasard des cartes
        self.shuffle()
        
        # Exécution des boutons
        self.shuffleButton.clicked.connect(self.shuffle)
        self.hitMeButton.clicked.connect(self.playerHit)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def shuffle(self):
        "Relance du jeu"
        
        "Réinitialisation du jeu (remise à 0)"
        
        # Suppression des cartes complémentaires dans le jeu
        pixmap = QPixmap('images/cards/green.png')
        self.dealerCard1.setPixmap(pixmap)
        self.dealerCard2.setPixmap(pixmap)
        self.dealerCard3.setPixmap(pixmap)
        self.dealerCard4.setPixmap(pixmap)
        self.dealerCard5.setPixmap(pixmap)
        self.playerCard1.setPixmap(pixmap)
        self.playerCard2.setPixmap(pixmap)
        self.playerCard3.setPixmap(pixmap)
        self.playerCard4.setPixmap(pixmap)
        self.playerCard5.setPixmap(pixmap)
        
        # Assignation d'une liste des enseignes des cartes
        suits = ['diamonds', 'clubs', 'hearts', 'spades']
        
        # Assignation d'une liste d'un nombre de cartes par enseignes
        values = range(2, 15) # de la carte '2' à la carte 'As'
        # 11 = Valet, 12 = Dame, 13 = Roi, 14 = As
        
        # Assignation des cartes du jeu 
        # (voir le nom du fichier de chaque image)
        self.deck = []
        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")
                
        # Assignation d'une liste des cartes des participants
        self.dealer = []
        self.player = []
        
        # Nombre de cartes par participant
        self.playerSpot = 0
        self.dealerSpot = 0
        
        # Pose de deux cartes par participant
        self.dealerHit()
        self.dealerHit()
        self.playerHit()
        self.playerHit()
        
    def dealCards(self):
        "Pose des cartes"
        
        try:
        
            "Côté distributeur"
            
            # Affichage au hasard d'une carte
            card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(card)
            
            # Ajout d'une carte au distributeur
            self.dealer.append(card)
            
            # Récupération d'une des images dans le dossier concerné
            pixmap = QPixmap(f'images/cards/{card}.png')
            
            # Insertion de l'image auprès du distributeur dans le GUI
            self.dealerCard1.setPixmap(pixmap)
            
            "Côté joueur"
            
            # Affichage au hasard d'une carte
            card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(card)
            
            # Ajout d'une carte au joueur
            self.player.append(card)
            
            # Récupération d'une des images dans le dossier concerné
            pixmap = QPixmap(f'images/cards/{card}.png')
            
            # Insertion de l'image auprès du joueur dans le GUI
            self.playerCard1.setPixmap(pixmap)
            
            "Modification du titre de la fenêtre"
            
            # Modification du titre de la fenêtre
            self.setWindowTitle(
                f"Il ne reste plus que {len(self.deck)} cartes")
        
        except IndexError:
            # Dès qu'il n'y a plus de cartes dans le jeu...
            
            # Modification du titre de la fenêtre
            self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
            
    def dealerHit(self):
        
        # Si le nombre de cartes jouées est < à 5
        if self.dealerSpot < 5:
            try:
                "Côté joueur"
                # Affichage au hasard d'une carte
                card = random.choice(self.deck)
                # Suppression de la carte jouée dans la liste
                self.deck.remove(card)
                # Ajout d'une carte au joueur
                self.dealer.append(card)
                # Récupération d'une des images dans le dossier concerné
                pixmap = QPixmap(f'images/cards/{card}.png')
                
                if self.dealerSpot == 0:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.dealerCard1.setPixmap(pixmap)
                    self.dealerSpot += 1
                    
                elif self.dealerSpot == 1:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.dealerCard2.setPixmap(pixmap)
                    self.dealerSpot += 1
                    
                elif self.dealerSpot == 2:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.dealerCard3.setPixmap(pixmap)
                    self.dealerSpot += 1
                    
                elif self.dealerSpot == 3:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.dealerCard4.setPixmap(pixmap)
                    self.dealerSpot += 1
                    
                elif self.dealerSpot == 4:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.dealerCard5.setPixmap(pixmap)
                    self.dealerSpot += 1
                
                "Modification du titre de la fenêtre"
                # Modification du titre de la fenêtre
                self.setWindowTitle(
                    f"Il ne reste plus que {len(self.deck)} cartes")
            
            except IndexError:
                # Dès qu'il n'y a plus de cartes dans le jeu...
                
                # Modification du titre de la fenêtre
                self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
    
    def playerHit(self):
        
        # Si le nombre de cartes jouées est < à 5
        if self.playerSpot < 5:
            try:
                "Côté joueur"
                # Affichage au hasard d'une carte
                card = random.choice(self.deck)
                # Suppression de la carte jouée dans la liste
                self.deck.remove(card)
                # Ajout d'une carte au joueur
                self.player.append(card)
                # Récupération d'une des images dans le dossier concerné
                pixmap = QPixmap(f'images/cards/{card}.png')
                
                if self.playerSpot == 0:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.playerCard1.setPixmap(pixmap)
                    self.playerSpot += 1
                    
                elif self.playerSpot == 1:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.playerCard2.setPixmap(pixmap)
                    self.playerSpot += 1
                    
                elif self.playerSpot == 2:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.playerCard3.setPixmap(pixmap)
                    self.playerSpot += 1
                    
                elif self.playerSpot == 3:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.playerCard4.setPixmap(pixmap)
                    self.playerSpot += 1
                    
                elif self.playerSpot == 4:
                    # Insertion de l'image auprès du joueur dans le GUI
                    self.playerCard5.setPixmap(pixmap)
                    self.playerSpot += 1
                
                "Modification du titre de la fenêtre"
                # Modification du titre de la fenêtre
                self.setWindowTitle(
                    f"Il ne reste plus que {len(self.deck)} cartes")
            
            except IndexError:
                # Dès qu'il n'y a plus de cartes dans le jeu...
                
                # Modification du titre de la fenêtre
                self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
        
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