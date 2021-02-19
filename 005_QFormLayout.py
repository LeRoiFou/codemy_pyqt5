"""
PyQt5 - Codemy.com #005 : How To Build Forms With QFormLayout - PyQt5 GUI Thursdays #5
Lien : https://www.youtube.com/watch?v=Lyph52xJe7U

Dans ce programme on apprend à créer un formulaire avec le widget QFormLayout : ce 'formulaire' permet de mettre à la
verticale un par un les widgets souhaités

Éditeur : Laurent REYNAUD
Date : 19-02-21
"""

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):

    def __init__(self):
        """Constructeur de la classe"""
        super().__init__()
        # """Configuration de la fenêtre principale à la verticale"""
        # self.setLayout(qtw.QVBoxLayout())
        """Ajout d'un titre à la fenêtre"""
        self.setWindowTitle('Build forms with QFormLayout')
        """Configuration du formulaire"""
        form_layout = qtw.QFormLayout()
        self.setLayout(form_layout)
        """Configuration d'une étiquette avec mise en forme"""
        label_1 = qtw.QLabel("C'est un titre")  # configuration
        label_1.setFont(qtg.QFont('Helvetica', 24))  # mise en forme
        """Configuration des champs de saisies"""
        f_name = qtw.QLineEdit(self)  # champ de saisie pour le prénom
        l_name = qtw.QLineEdit(self)  # champ de saisie pour le nom
        """Ajout des lignes dont le widget QLabel"""
        form_layout.addRow(label_1)  # ajout de l'étiquette
        form_layout.addRow("Prénom", f_name)  # ajout du champ de saisie 'prénom'
        form_layout.addRow("Nom", l_name)  # ajout du champ de saisie 'nom'
        form_layout.addRow(qtw.QPushButton('Appuie !', clicked=lambda: press_it()))  # ajout d'un bouton
        """Affichage de la fenêtre"""
        self.show()

        def press_it():
            label_1.setText(f"Tu as cliqué sur le bouton, {f_name.text()} {l_name.text()}!")


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
