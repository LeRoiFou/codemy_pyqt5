"""
Cours : CheckBoxes - PyQt5 GUI Thursdays #20
Lien : https://www.youtube.com/watch?v=11iUOBqqjtU

On a recours au widget checkBoxes qui est similaire
au widget radioButton mais cette fois-ci il n'est pas nécessaire
de faire un choix

Même cours que le précédent mais cette fois-ci nous n'avons pas de bouton
d'exécution...

Editeur : Laurent REYNAUD
Date : 24-06-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        "Configuration des widgets"
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 281)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Checkbox : rouge
        self.red_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.red_checkBox.setGeometry(QtCore.QRect(110, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.red_checkBox.setFont(font)
        self.red_checkBox.setObjectName("red_checkBox")
        # self.red_checkBox.setChecked(True) # sélection par défaut
        
         # Connection avec l'option choisie : Rouge
        self.red_checkBox.toggled.connect(
            lambda: self.checked())
        
        # Checkbox : bleu
        self.blue_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.blue_checkBox.setGeometry(QtCore.QRect(110, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.blue_checkBox.setFont(font)
        self.blue_checkBox.setObjectName("blue_checkBox")  
        
        # Connection avec l'option choisie : Bleu
        self.blue_checkBox.toggled.connect(
            lambda: self.checked())
        
        # Titre
        self.my_label = QtWidgets.QLabel(self.centralwidget)
        self.my_label.setGeometry(QtCore.QRect(110, 150, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_label.setFont(font)
        self.my_label.setObjectName("my_label")
        
        # Barre de menus      
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Barre de statuts
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        "Textes rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.red_checkBox.setText(_translate("MainWindow", "Rouge"))
        self.blue_checkBox.setText(_translate("MainWindow", "Bleu"))
        # self.my_button.setText(_translate("MainWindow", "Soumettre"))
        self.my_label.setText(_translate("MainWindow", "Choisis une couleur"))
        
    def checked(self):
        """Méthode affichant l'option choisie :
        La fonctionnalité n'est pas la même que pour le widget
        radioButtons (voir index019_radioButtons) car avec ce widget
        l'utilisateur peut choisir de ne rien opter contrairement au
        widget radio button mais la raison principale pour laquelle
        les instructions ne sont pas les mêmes est que l'utilisateur
        peut choisir plusieurs options alors que pour le widget
        radio button l'utilisateur ne peut choisir qu'une option..."""
                
        # Si l'option 'Rouge' est cochée...
        if self.red_checkBox.isChecked() == True:
            self.red = 'Rouge'
        else:
            self.red = ''
        
        # # Si l'option 'Bleu' est cochée...
        if self.blue_checkBox.isChecked() == True:
            self.blue = 'Bleu'
        else:
            self.blue = ''

        # Texte à afficher
        self.my_label.setText(f"{self.red} {self.blue}")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
