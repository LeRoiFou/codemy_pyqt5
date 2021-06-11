"""
Cours : Radio Buttons - PyQt5 GUI Thursdays #18
Lien : https://www.youtube.com/watch?v=emwXHvtAYzs

Ce programme permet d'afficher une liste d'option (ici le choix de pizzas)
Deux instructions sont spécifique à ce widget :
-> setChecked(True) : sélection par défaut de l'option
-> isChecked() : si l'option est cochée...

Editeur : Laurent REYNAUD
Date : 11-06-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pizzas(object):
    
    def setupUi(self, Pizzas):
        "Configuration des widgets"
        
        Pizzas.setObjectName("Pizzas")
        Pizzas.resize(556, 405)
        self.centralwidget = QtWidgets.QWidget(Pizzas)
        self.centralwidget.setObjectName("centralwidget")
        Pizzas.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pizzas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 26))
        self.menubar.setObjectName("menubar")
        Pizzas.setMenuBar(self.menubar)
        
        # Option Calzone
        self.radioButton_calzone = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_calzone.setGeometry(QtCore.QRect(170, 20, 173, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_calzone.setFont(font)
        self.radioButton_calzone.setObjectName("radioButton_calzone")
        
        # Sélection par défaut de la Calzone
        self.radioButton_calzone.setChecked(True)
        
        # Option Jambon
        self.radioButton_ham = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_ham.setGeometry(QtCore.QRect(170, 70, 120, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_ham.setFont(font)
        self.radioButton_ham.setObjectName("radioButton_ham")
        
        # Option Champignons
        self.radioButton_mushrooms = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_mushrooms.setGeometry(QtCore.QRect(170, 120, 188, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_mushrooms.setFont(font)
        self.radioButton_mushrooms.setObjectName("radioButton_mushrooms")
        
        # Bouton d'exécution
        self.my_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.select())
        self.my_button.setGeometry(QtCore.QRect(150, 200, 211, 42))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_button.setFont(font)
        self.my_button.setObjectName("my_button")
        
        # Texte
        self.my_label = QtWidgets.QLabel(self.centralwidget)
        self.my_label.setGeometry(QtCore.QRect(150, 280, 207, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_label.setFont(font)
        self.my_label.setObjectName("my_label")

        # Barre de statut
        self.statusbar = QtWidgets.QStatusBar(Pizzas)
        self.statusbar.setObjectName("statusbar")
        Pizzas.setStatusBar(self.statusbar)

        self.retranslateUi(Pizzas)
        QtCore.QMetaObject.connectSlotsByName(Pizzas)

    def retranslateUi(self, Pizzas):
        "Textes rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        
        Pizzas.setWindowTitle(_translate("Pizzas", "MainWindow"))
        
        self.radioButton_calzone.setText(_translate("Pizzas", "Calzone"))
        self.radioButton_ham.setText(_translate("Pizzas", "Jambon"))
        self.radioButton_mushrooms.setText(_translate("Pizzas", "Champignons"))
        self.my_button.setText(_translate("Pizzas", "Sélection"))
        self.my_label.setText(_translate("Pizzas", "Faites votre choix"))
        
    def select(self):
        "Méthode permettant d'afficher la pizza choisie et de la valider"
        
        if self.radioButton_calzone.isChecked():
            # Affichage de la pizza choisie
            self.my_label.setText(self.radioButton_calzone.text())
            # Les textes des autres choix sont effacés
            self.radioButton_ham.setText("")
            self.radioButton_mushrooms.setText("")
            # Sélection par défaut du Jambon
            self.radioButton_ham.setChecked(True)
        elif self.radioButton_ham.isChecked():
            # Affichage de la pizza choisie
            self.my_label.setText(self.radioButton_ham.text())
            # Modification du texte du choix du Jambon
            self.radioButton_ham.setText("Validé !")
        elif self.radioButton_mushrooms.isChecked():
            # Affichage de la pizza choisie
            self.my_label.setText(self.radioButton_mushrooms.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pizzas = QtWidgets.QMainWindow()
    ui = Ui_Pizzas()
    ui.setupUi(Pizzas)
    Pizzas.show()
    sys.exit(app.exec_())
