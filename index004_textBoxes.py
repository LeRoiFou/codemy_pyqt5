"""
PyQt5 - Codemy.com #4 : How To Create Text Boxes - PyQt5 GUI Thursdays #4
Lien : https://www.youtube.com/watch?v=Fl92v4PpbzE

Dans ce programme on apprend à créer une zone de texte avec de multiples configurations...
On a plus de possibilités qu'avec un TextBox de l'interface graphique tkinter

Éditeur : Laurent REYNAUD
Date : 12-02-2021
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
        my_label = qtw.QLabel('Choisis une donnée du menu')
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)
        """Configuration de la zone de liste"""
        my_text = qtw.QTextEdit(self,
                                # plainText="C'est un vrai texte",  # affichage du texte par défaut en 1ère ligne
                                # html="<center><h1><em>Gros titre</em></h1></center>",  # affichage format html
                                acceptRichText=True,  # copie la mise en forme issue, par ex, d'un fichier Writer
                                lineWrapMode=qtw.QTextEdit.FixedColumnWidth,  # retour à la ligne automatique
                                lineWrapColumnOrWidth=50,  # nombre de caractères par ligne
                                placeholderText="Hello World !",  # affichage texte brouillon par défaut en 1ere ligne
                                readOnly=False  # True : lecture seulement, pas de possibilité de saisir
                                )
        """Ajout de la zone de liste dans la fenêtre principale"""
        self.layout().addWidget(my_text)
        """Configuration d'un bouton d'exécution"""
        my_button = qtw.QPushButton('Appuie-moi !', clicked=lambda: press_it())
        self.layout().addWidget(my_button)
        """Affichage de la fenêtre"""
        self.show()

        def press_it():
            """Fonction permettant de modifier le texte après avoir validé la saisie faite dans la zone de texte"""
            my_label.setText(f"Tu as choisi : {my_text.toPlainText()} !")  # affichage de la donnée à l'étiquette
            my_text.setPlainText("Tu as appuyé sur le bouton !")  # affichage de la donnée dans la zone de texte


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
