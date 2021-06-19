"""
Cours : Radio Buttons Without Push Buttons - PyQt5 GUI Thursdays #19
Lien : https://www.youtube.com/watch?v=m7sAJZPDdAY

Même cours que le précédent mais cette fois-ci nous n'avons pas de bouton
d'exécution...

Editeur : Laurent REYNAUD
Date : 19-06-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pizzas(object):
    
    def setupUi(self, Pizzas):
        "Configuration des widgets"
        
        Pizzas.setObjectName("Pizzas")
        Pizzas.resize(556, 268)
        self.centralwidget = QtWidgets.QWidget(Pizzas)
        self.centralwidget.setObjectName("centralwidget")
        Pizzas.setCentralWidget(self.centralwidget)
        
        # Option Calzone
        self.radioButton_calzone = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_calzone.setGeometry(QtCore.QRect(170, 20, 173, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_calzone.setFont(font)
        self.radioButton_calzone.setObjectName("radioButton_calzone")
        
        # Option Jambon
        self.radioButton_ham = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_ham.setGeometry(QtCore.QRect(170, 70, 120, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_ham.setFont(font)
        self.radioButton_ham.setObjectName("radioButton_ham")
        
        # Sélection par défaut d'une des options
        self.radioButton_calzone.setChecked(True)
        
        # Option Champignons
        self.radioButton_mushrooms = QtWidgets.QRadioButton(
            self.centralwidget)
        self.radioButton_mushrooms.setGeometry(QtCore.QRect(
            170, 120, 188, 37))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_mushrooms.setFont(font)
        self.radioButton_mushrooms.setObjectName("radioButton_mushrooms")
        
        # Affichage de l'option choisie
        self.my_label = QtWidgets.QLabel(self.centralwidget)
        self.my_label.setGeometry(QtCore.QRect(160, 180, 230, 33))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_label.setFont(font)
        self.my_label.setObjectName("my_label")
            
        # Barre de menu
        self.menubar = QtWidgets.QMenuBar(Pizzas)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 26))
        self.menubar.setObjectName("menubar")
        Pizzas.setMenuBar(self.menubar)
        
        # Barre de sstatut
        self.statusbar = QtWidgets.QStatusBar(Pizzas)
        self.statusbar.setObjectName("statusbar")
        Pizzas.setStatusBar(self.statusbar)

        self.retranslateUi(Pizzas)
        QtCore.QMetaObject.connectSlotsByName(Pizzas)
        
        "Connection de l'option choisie avec la méthode btnstate()"
        
        # Connection avec l'option choisie : Calzone
        self.radioButton_calzone.toggled.connect(
            lambda: self.btnstate(self.radioButton_calzone))
        
         # Connection avec l'option choisie : Jambon
        self.radioButton_ham.toggled.connect(
            lambda: self.btnstate(self.radioButton_ham))
        
         # Connection avec l'option choisie : Champignons
        self.radioButton_mushrooms.toggled.connect(
            lambda: self.btnstate(self.radioButton_mushrooms))
        
    def retranslateUi(self, Pizzas):
        "Textes rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        
        Pizzas.setWindowTitle(_translate("Pizzas", "MainWindow"))
        self.radioButton_calzone.setText(_translate(
            "Pizzas", "Calzone"))
        self.radioButton_ham.setText(_translate(
            "Pizzas", "Jambon"))
        self.radioButton_mushrooms.setText(_translate(
            "Pizzas", "Champignons"))
        self.my_label.setText(_translate("Pizzas", "Faites votre choix"))

    def btnstate(self, b):
        """Méthode qui affiche l'option choisie :
        le paramètre 'b' est associé aux widgets self.raddioButton_XXX
        qui sont argumentés lors de l'appel de la méthode ci-dessus"""
        
        # Si une des options est choisie...
        if b.isChecked():
            
            # Si l'option choisie est la Calzone
            if b.text() == "Calzone":
                
                # Affichage de la phrase suivante
                self.my_label.setText("J'adore la Calzone !!!")
            
            # Sinon si l'option choisie n'est pas la Calzone
            else:
                
                # Affichage de la pizza choisie
                self.my_label.setText(b.text())
              

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pizzas = QtWidgets.QMainWindow()
    ui = Ui_Pizzas()
    ui.setupUi(Pizzas)
    Pizzas.show()
    sys.exit(app.exec_())
