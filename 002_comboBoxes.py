"""
PyQt5 - Codemy.com #2 : How To Create Combo Boxes - PyQt5 GUI Thursdays #2
Lien : https://www.youtube.com/watch?v=O58FGYYBV7U

Dans ce programme on apprend à crééer un menu déroulant avec différents paramétrages

Éditeur : Laurent REYNAUD
Date : 29-01-21
"""

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self):
        """Constructeur de la classe"""
        super().__init__()
        """Configuration de la fenêtre principale à la verticale"""
        self.setLayout(qtw.QVBoxLayout())
        """Ajout d'un titre à la fenêtre"""
        self.setWindowTitle('Titre !')
        """Configuration d'une étiquette"""
        my_label = qtw.QLabel('Choisis une donnée du menu déroulant')
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        """Configuration d'un menu déroulant"""
        my_combo = qtw.QComboBox(self,
                                 editable=True,  # saisie modifiable dans le menu déroulant
                                 # insertPolicy=qtw.QComboBox.InsertAtTop  # insertion à la 1ère ligne
                                 insertPolicy=qtw.QComboBox.InsertAtBottom  # insertion à la dernière ligne
                                 )
        """Ajout d'articles au menu déroulant avec pour certains éléments 2 données"""
        my_combo.addItem('Calzone', 'Machin')  # ajout d'un article dans le menu déroulant
        my_combo.addItem('4 fromages', 2)  # ajout de la donnée dans le menu déroulant
        my_combo.addItem('Champignons', qtw.QWidget)  # ajout d'un article dans le menu déroulant
        my_combo.addItem('Poivrons')  # ajout d'un article dans le menu déroulant
        my_combo.addItems(['un', 'deux', 'trois'])  # ajout de cette liste d'articles dans le menu déroulant
        my_combo.insertItem(2, '3ème ligne')  # insertion de cet article à l'indice n° 2
        my_combo.insertItems(4, ['Truc', 'Marius'])  # insertion de ces articles à partir de l'indice n° 4
        """Ajout du menu déroulant dans la fenêtre principale"""
        self.layout().addWidget(my_combo)
        """Configuration d'un bouton d'exécution"""
        my_button = qtw.QPushButton('Appuie-moi !', clicked=lambda: press_it())
        self.layout().addWidget(my_button)
        """Affichage de la fenêtre"""
        self.show()

        def press_it():
            """Fonction permettant de modifier le texte après avoir validé la saisie faite dans le menu déroulant"""
            my_label.setText(f"Tu as choisi : {my_combo.currentText()} !")  # affichage de la première donnée
            # my_label.setText(f"Tu as choisi : {my_combo.currentData()} !")  # affichage de la deuxième donnée
            # my_label.setText(f"Tu as choisi : {my_combo.currentIndex()} !")  # affichage du n° d'indice de la donnée


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
