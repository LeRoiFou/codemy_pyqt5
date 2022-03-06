"""
Cours #51 : Blackjack Convert Aces To One Point
Lien : https://www.youtube.com/watch?v=f8OV2fidZsc

Jeu de cartes black jack (suite) : valeur de la carte 'As' vaut 1 point au lieu de 11

Editeur : Laurent REYNAUD
Date : 06-03-22
"""

import enum
from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QLabel, QPushButton, QDesktopWidget, QMessageBox
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
        
        # Réinitialisation du score obtenu par chaque participant
        self.player_total = 0
        self.dealer_total = 0
        
        # Assignation d'un dictionnaire des statuts des participants
        # au lancement du jeu aucun partipant gagne ("no")
        self.blackjack_status = {"dealer": "no", "player": "no"}
        
        # Réactivation des boutons
        self.hitMeButton.setEnabled(True)
        self.standButton.setEnabled(True)
        
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
        
        # Liste des scores attribués à chaque participant
        self.dealer_score = []
        self.player_score = []
        
        # Nombre de cartes par participant
        self.playerSpot = 0
        self.dealerSpot = 0
        
        # Pose de deux cartes par participant
        self.dealerHit() # 1ère carte posée côté dealer
        self.dealerHit() # 2ème carte posée côté dealer
        self.playerHit() # 1ère carte posée côté player
        self.playerHit() # 2ème carte posée côté dealer
        
    def dealerHit(self):
        "Jeu du 'dealer' : valeur de la carte posée et GUI"
        
        # Si le nombre de cartes jouées est < à 5
        if self.dealerSpot < 5:
            try:
                # Affichage au hasard d'une carte
                card = random.choice(self.deck)
                # Suppression de la carte jouée dans la liste
                self.deck.remove(card)
                # Ajout d'une carte au joueur
                self.dealer.append(card)
                
                # Récupération de la valeur de la carte posée 
                # (par ex : fichier carte 2_of_clubs.png = 2)
                # (par ex : fichier carte 12_of_diamonds.png = 12)
                self.dcard = int(card.split('_', 1)[0])
                
                # Si la valeur de la carte est 14 (As):
                if self.dcard == 14:
                    # Ajout du score de 11 points
                    self.dealer_score.append(11)
                # Si la valeur de la carte est 
                # 11 (Valet), ou 12 (Dame) ou 13 (Roi)
                elif self.dcard == 11 or self.dcard == 12 or self.dcard == 13:
                    # Ajout du score de 10 points
                    self.dealer_score.append(10)
                else:
                    self.dealer_score.append(self.dcard)
                
                # Récupération d'une des images dans le dossier concerné
                pixmap = QPixmap(f'images/cards/{card}.png')
                
                # GUI : selon le n° de la carte posée (5 cartes max posées)
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

                # Modification du titre de la fenêtre
                self.setWindowTitle(
                    f"Il ne reste plus que {len(self.deck)} cartes")
            
            except IndexError:
                # Dès qu'il n'y a plus de cartes dans le jeu...
                
                # Modification du titre de la fenêtre
                self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
                
            # Score final obtenu
            self.blackjack_check("Dealer")
    
    def playerHit(self):
        "Jeu du 'player' : valeur de la carte posée et GUI"
        
        # Si le nombre de cartes jouées est < à 5
        if self.playerSpot < 5:
            try:  
                # Affichage au hasard d'une carte
                card = random.choice(self.deck)
                # Suppression de la carte jouée dans la liste
                self.deck.remove(card)
                # Ajout d'une carte au joueur
                self.player.append(card)
                
                # Récupération de la valeur de la carte posée 
                # (par ex : fichier carte 2_of_clubs.png = 2)
                # (par ex : fichier carte 12_of_diamonds.png = 12)
                self.pcard = int(card.split('_', 1)[0])
                
                # Si la valeur de la carte est 14 (As):
                if self.pcard == 14:
                    # Ajout du score de 11 points
                    self.player_score.append(11)
                # Si la valeur de la carte est 
                # 11 (Valet), ou 12 (Dame) ou 13 (Roi)
                elif self.pcard == 11 or self.pcard == 12 or self.pcard == 13:
                    # Ajout du score de 10 points
                    self.player_score.append(10)
                else:
                    self.player_score.append(self.pcard)
                
                # Récupération d'une des images dans le dossier concerné
                pixmap = QPixmap(f'images/cards/{card}.png')
                
                # GUI : selon le n° de la carte posée (5 cartes max posées)
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
                
                # Modification du titre de la fenêtre
                self.setWindowTitle(
                    f"Il ne reste plus que {len(self.deck)} cartes")
            
            except IndexError:
                # Dès qu'il n'y a plus de cartes dans le jeu...
                
                # Modification du titre de la fenêtre
                self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
            
            # Score final obtenu
            self.blackjack_check("Player")
            
    def blackjack_check(self, gamer):
        "Score final obtenu pour chaque participant"
        
        # Réinitialisation du score obtenu par chaque participant
        self.player_total = 0
        self.dealer_total = 0
        
        # Changement de statuts des participants
        if gamer == 'Dealer':
            # Si le nombre de cartes posées est de 2
            if len(self.dealer_score) == 2:
                # Si la 1ère carte et la 2ème carte posée sont = à 21
                if self.dealer_score[0] + self.dealer_score[1] == 21:
                    # Changer le statut du dealer ("yes" = gagné)
                    self.blackjack_status["dealer"] = "yes"
                    
        if gamer == 'Player':
            # Si le nombre de cartes posées est de 2
            if len(self.player_score) == 2:
                # Si la 1ère carte et la 2ème carte posée sont = à 21
                if self.player_score[0] + self.player_score[1] == 21:
                    # Changer le statut du player ("yes" = gagné)
                    self.blackjack_status["player"] = "yes"
            # S'il y a plus de 2 cartes posées
            else:
                # Pour la valeur des points de chaque carte posée au jeu
                for score in self.player_score:
                    # Incrémentation de cette valeur
                    self.player_total += score
                # Si le score total obtenu est de 21
                if self.player_total == 21:
                    self.blackjack_status['player'] = 'yes'
                # Si le score total obtenu est > à 21
                elif self.player_total > 21:
                    # Conversion de la valeur de la carte 'As'
                    for card_num, card in enumerate(self.player_score):
                        if card == 11:
                            self.player_score[card_num] = 1
                            # Mise à jour du score total obtenu
                            self.player_total = 0
                            for score in self.player_score:
                                self.player_total += score
                            # Vérification du statut du joueur
                            if self.player_total > 21:
                                self.blackjack_status['player'] = 'bust'  
                    # À défaut de la conversion de la valeur de la carte 'As'              
                    else:
                        if self.player_total == 21:
                            self.blackjack_status['player'] = 'yes'
                        if self.player_total > 21:
                            self.blackjack_status['player'] = 'bust'
                    
                    # self.blackjack_status['player'] = 'bust'
                    
        # Si chaque participant a 2 cartes posées
        if len(self.player_score) == 2 and len(self.dealer_score) == 2:
            
            # Et si chaque partipant a gagné
            if (self.blackjack_status["dealer"] == "yes" 
                and self.blackjack_status["player"] == "yes"):
                    # Message d'égalité
                    QMessageBox.about(self, 
                                      "Push!",
                                      "It's a tie!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            
            # Si c'est le dealer qui a gagné
            elif self.blackjack_status["dealer"] == "yes":
                    # Message de victoire du dealer
                    QMessageBox.about(self, 
                                      "Dealer wins!",
                                      "Blackjack! Dealer wins!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            
            # Si c'est le player qui a gagné
            elif self.blackjack_status["player"] == "yes":
                    # Message de victoire du player
                    QMessageBox.about(self, 
                                      "Player wins!",
                                      "Blackjack! Player wins!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
                    
        # À défaut
        else:            
            
            # Si chaque partipant a gagné
            if (self.blackjack_status["dealer"] == "yes" 
                and self.blackjack_status["player"] == "yes"):
                    # Message d'égalité
                    QMessageBox.about(self, 
                                      "Push!",
                                      "It's a tie!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            
            # Si c'est le dealer qui a gagné
            elif self.blackjack_status["dealer"] == "yes":
                    # Message de victoire du dealer
                    QMessageBox.about(self, 
                                      "Dealer wins!",
                                      "21! Dealer wins!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
            
            # Si c'est le player qui a gagné
            elif self.blackjack_status["player"] == "yes":
                    # Message de victoire du player
                    QMessageBox.about(self, 
                                      "Player wins!",
                                      "21! Player wins!")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
                    
        # Si le 'player' a perdu
        if self.blackjack_status['player'] == 'bust':
            # Message de défaite du player
                    QMessageBox.about(self, 
                                      "Bust!",
                                      f"Player loses: {self.player_total}")
                    # Désactivation des boutons
                    self.hitMeButton.setEnabled(False)
                    self.standButton.setEnabled(False)
        
    def center(self):
        "Application centrée sur l'écran"
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    # def dealCards(self):
    #     "Pose des cartes"
        
    #     try:
        
    #         "Côté distributeur"
            
    #         # Affichage au hasard d'une carte
    #         card = random.choice(self.deck)
            
    #         # Suppression de la carte jouée dans la liste
    #         self.deck.remove(card)
            
    #         # Ajout d'une carte au distributeur
    #         self.dealer.append(card)
            
    #         # Récupération d'une des images dans le dossier concerné
    #         pixmap = QPixmap(f'images/cards/{card}.png')
            
    #         # Insertion de l'image auprès du distributeur dans le GUI
    #         self.dealerCard1.setPixmap(pixmap)
            
    #         "Côté joueur"
            
    #         # Affichage au hasard d'une carte
    #         card = random.choice(self.deck)
            
    #         # Suppression de la carte jouée dans la liste
    #         self.deck.remove(card)
            
    #         # Ajout d'une carte au joueur
    #         self.player.append(card)
            
    #         # Récupération d'une des images dans le dossier concerné
    #         pixmap = QPixmap(f'images/cards/{card}.png')
            
    #         # Insertion de l'image auprès du joueur dans le GUI
    #         self.playerCard1.setPixmap(pixmap)
            
    #         "Modification du titre de la fenêtre"
            
    #         # Modification du titre de la fenêtre
    #         self.setWindowTitle(
    #             f"Il ne reste plus que {len(self.deck)} cartes")
        
    #     except IndexError:
    #         # Dès qu'il n'y a plus de cartes dans le jeu...
            
    #         # Modification du titre de la fenêtre
    #         self.setWindowTitle("Il ne reste plus de cartes dans le jeu...")
            
        
# Exécution de l'application
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()