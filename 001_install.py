"""
PyQt5 - Codemy.com #1 : Install PyQt5 And Build Simple GUI App - PyQt5 GUI Thursdays #1
Lien : https://www.youtube.com/watch?v=rZcdhles6vQ

Dans ce programme on apprend à utiliser PyQt5 qui est une interface graphique comme Tkinter en insérant :
-> Un titre de la fenêtre principale
-> Une étiquette
-> Un champ de saisie
-> Un bouton
Package installé : PyQt5

Éditeur : Laurent REYNAUD
Date : 22-01-21
"""

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg  # police d'écriture


class MainWindow(qtw.QWidget):

    def __init__(self):
        """Constructeur de la classe"""
        super().__init__()
        """Ajout d'un titre à la fenêtre"""
        self.setWindowTitle('Hello World !')
        """Configuration de la fenêtre principale à la verticale"""
        self.setLayout(qtw.QVBoxLayout())
        """"Configuration d'une étiquette"""
        my_label = qtw.QLabel('Salut ! Quel est ton nom ?')
        my_label.setFont(qtg.QFont('Helvetica', 18))  # changement de la taille d'écriture
        self.layout().addWidget(my_label)  # ajout de l'étiquette dans la fenêtre principale
        """Configuration d'un champ de saisie"""
        my_entry = qtw.QLineEdit()
        # my_entry.setObjectName('Champ du nom')  # ???
        my_entry.setText('')  # texte par défaut dans le champ de saisie
        self.layout().addWidget(my_entry)  # ajout du champ de saisie dans la fenêtre principale
        """Configuration d'un bouton"""
        my_button = qtw.QPushButton('Appuie-moi !', clicked=lambda: press_it())
        self.layout().addWidget(my_button)  # ajout du bouton dans la fenêtre principale
        """Affichage de la fenêtre principale et des widgets"""
        self.show()

        def press_it():
            """Fonction permettant de modifier le texte dans le widget label et de réinitialiser le champ de saisie"""
            my_label.setText(f"Salut {my_entry.text()} !")
            my_entry.setText('')  # réinitialisation du champ de saisie


app = qtw.QApplication([])
mw = MainWindow()  # instanciation de la classe ci-dessus

app.exec_()
