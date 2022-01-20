"""
Cours #45 : Create And Deal A Deck Of Cards
Lien : https://www.youtube.com/watch?v=CuO8-uG4UVI

Dans ce programme on apprend à créer un jeu de cartes ;)

Editeur : Laurent REYNAUD
Date : 20-01-22
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
        uic.loadUi('index045_JeuCartes.UI', self)
        
        # Configuration des widgets
        self.label_dealer = self.findChild(QLabel, "dealer_label")
        self.label_player = self.findChild(QLabel, "player_label")
        self.label_dealer_card = self.findChild(QLabel, "dealer_card_label")
        self.label_player_card = self.findChild(QLabel, "player_card_label")
        self.shuffle_button = self.findChild(QPushButton, "shuffle_button")
        self.deal_button = self.findChild(QPushButton, "deal_button")
        
        # Dès le lancement du jeu, affichage au hasard des cartes
        self.shuffle()
        
        # Exécution des boutons
        self.shuffle_button.clicked.connect(self.shuffle)
        self.deal_button.clicked.connect(self.dealCards)
        
        # Affichage de l'application
        self.center()
        self.show()
        
    def shuffle(self):
        "Relance du jeu"
        
        "Réinitialisation du jeu (remise à 0)"
        
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
        
        "Côté distributeur"
        
        # Affichage au hasard d'une carte
        card = random.choice(self.deck)

        # Ajout d'une carte au distributeur
        self.dealer.append(card)
        
        # Récupération d'une des images dans le dossier concerné
        pixmap = QPixmap(f'images/cards/{card}.png')
        
        # Insertion de l'image auprès du distributeur dans le GUI
        self.label_dealer_card.setPixmap(pixmap)
        
        "Côté joueur"
        
        # Affichage au hasard d'une carte
        card = random.choice(self.deck)
        
        # Ajout d'une carte au joueur
        self.player.append(card)
        
        # Récupération d'une des images dans le dossier concerné
        pixmap = QPixmap(f'images/cards/{card}.png')
        
        # Insertion de l'image auprès du joueur dans le GUI
        self.label_player_card.setPixmap(pixmap)
        
        "Modification du titre de la fenêtre"
        
        self.setWindowTitle(
            f"Jeu de {len(self.deck)} cartes ;)")
        
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
            self.label_dealer_card.setPixmap(pixmap)
            
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
            self.label_player_card.setPixmap(pixmap)
            
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