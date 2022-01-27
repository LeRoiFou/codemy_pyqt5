"""
Cours #46 : Create The Card Game "War"
Lien : https://www.youtube.com/watch?v=ANzji_8xWNc

Dans ce programme on apprend à créer un jeu de cartes ;)
Cette fois-ci on créé le jeu de bataille navale

Editeur : Laurent REYNAUD
Date : 27-01-22
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
        
        # Remise à 0 du compteur de score
        self.dealer_score = 0
        self.player_score = 0
        
        "Côté distributeur"
        
        # Affichage au hasard d'une carte
        self.dealer_card = random.choice(self.deck)

        # Ajout d'une carte au distributeur
        self.dealer.append(self.dealer_card)
        
        # Récupération d'une des images dans le dossier concerné
        pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
        
        # Insertion de l'image auprès du distributeur dans le GUI
        self.label_dealer_card.setPixmap(pixmap)
        
        "Côté joueur"
        
        # Affichage au hasard d'une carte
        self.player_card = random.choice(self.deck)
        
        # Ajout d'une carte au joueur
        self.player.append(self.player_card)
        
        # Récupération d'une des images dans le dossier concerné
        pixmap = QPixmap(f'images/cards/{self.player_card}.png')
        
        # Insertion de l'image auprès du joueur dans le GUI
        self.label_player_card.setPixmap(pixmap)
        
        "Modification du titre de la fenêtre"
        
        self.setWindowTitle(
            f"Jeu de {len(self.deck)} cartes ;)")
        
        # Affichage du score
        self.score()
        
    def dealCards(self):
        "Pose des cartes"
        
        try:
        
            "Côté distributeur"
            
            # Affichage au hasard d'une carte
            self.dealer_card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(self.dealer_card)
            
            # Ajout d'une carte au distributeur
            self.dealer.append(self.dealer_card)
            
            # Récupération d'une des images dans le dossier concerné
            pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
            
            # Insertion de l'image auprès du distributeur dans le GUI
            self.label_dealer_card.setPixmap(pixmap)
            
            "Côté joueur"
            
            # Affichage au hasard d'une carte
            self.player_card = random.choice(self.deck)
            
            # Suppression de la carte jouée dans la liste
            self.deck.remove(self.player_card)
            
            # Ajout d'une carte au joueur
            self.player.append(self.player_card)
            
            # Récupération d'une des images dans le dossier concerné
            pixmap = QPixmap(f'images/cards/{self.player_card}.png')
            
            # Insertion de l'image auprès du joueur dans le GUI
            self.label_player_card.setPixmap(pixmap)
            
            "Modification du titre de la fenêtre"
            
            # Modification du titre de la fenêtre
            self.setWindowTitle(
                f"Il ne reste plus que {len(self.deck)} cartes")
            
            # Affichage du score
            self.score()
        
        except IndexError:
            # Dès qu'il n'y a plus de cartes dans le jeu...
            
            if self.dealer_score == self.player_score:
                self.setWindowTitle(f"Fin du jeu ! || Ex-aequo !  {self.dealer_score} à {self.player_score}")
            elif self.dealer_score > self.player_score:
                self.setWindowTitle(f"Fin du jeu ! || Ordi a gagné !  {self.dealer_score} à {self.player_score}")
            else:
                self.setWindowTitle(f"Fin du jeu ! || Joueur a gagné !  {self.player_score} à {self.dealer_score}")
            
    def score(self):
        "Affichage du score"
        
        # Récupération du numéro de la carte
        self.dealer_card = int(self.dealer_card.split('_', 1)[0])
        self.player_card = int(self.player_card.split('_', 1)[0])
        
        # Comparaison des numéros des cartes affichés et affichage du score
        if self.dealer_card == self.player_card:
            self.label_dealer.setText("Ex-aequo !")
            self.label_player.setText("Ex-aequo !")
            self.setWindowTitle(
                f"{len(self.deck)} cartes restantes dans le jeu   ||   Ordi : {self.dealer_score}    Joueur : {self.player_score}")
        elif self.dealer_card > self.player_card:
            self.label_dealer.setText("Ordi a gagné !")
            self.label_player.setText("Joueur nullos !")
            self.dealer_score += 1
            self.setWindowTitle(
                f"{len(self.deck)} cartes restantes dans le jeu   ||   Ordi : {self.dealer_score}    Joueur : {self.player_score}")
        else:
            self.label_dealer.setText("Ordi craignos !")
            self.label_player.setText("Bravo joueur !")
            self.player_score += 1
            self.setWindowTitle(
                f"{len(self.deck)} cartes restantes dans le jeu   ||   Ordi : {self.dealer_score}    Joueur : {self.player_score}")
        
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