"""
PyQt5 - Codemy.com #3 : How To Create Spin Boxes - PyQt5 GUI Thursdays #3
Lien : https://www.youtube.com/watch?v=2NyculhiSh4

Dans ce programme on apprend à crééer un spinboxes qui est un champ de saisi sur une seule ligne avec au bout de ce
widgets une 'mini' barre de défilement (similaire au cours de tkinter n° 98)

Éditeur : Laurent REYNAUD
Date : 05-02-2021
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
        # """Configuration d'un spin boxes pour les valeurs en entier"""
        # my_spin = qtw.QSpinBox(self,
        #                        value=10,
        #                        maximum=100,
        #                        minimum=0,
        #                        singleStep=20,
        #                        prefix='#',
        #                        suffix=' Order'
        #                        )
        """Configuration d'un spin boses pour les valeurs en réel"""
        my_spin = qtw.QDoubleSpinBox(self,
                                     value=10.5,
                                     maximum=100,
                                     minimum=0,
                                     singleStep=5.50,
                                     prefix='#',
                                     suffix=' Order'
                                     )
        """Changement de la police d'écriture du spin boxes"""
        my_spin.setFont(qtg.QFont('Helivetica', 18))
        """Ajout du spin boxes dans la fenêtre principale"""
        self.layout().addWidget(my_spin)
        """Configuration d'un bouton d'exécution"""
        my_button = qtw.QPushButton('Appuie-moi !', clicked=lambda: press_it())
        self.layout().addWidget(my_button)
        """Affichage de la fenêtre"""
        self.show()

        def press_it():
            """Fonction permettant de modifier le texte après avoir validé la saisie faite dans le menu déroulant"""
            my_label.setText(f"Tu as choisi : # {my_spin.value()} Order !")  # affichage de la donnée


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()
