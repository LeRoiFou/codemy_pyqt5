"""
Cours : Designer Combo Boxes - PyQt5 GUI Thursdays #23
Lien : https://www.youtube.com/watch?v=31QT25J_cec

Dans ce programme on apprend à crééer un menu déroulant 
avec différents paramétrages (idem que l'index002) mais cette fois-ci
avec l'application Designer

Editeur : Laurent REYNAUD
Date : 02-08-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        "Configuration des widgets"
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Titre
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 661, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Menu déroulant
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 110, 441, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        
        # Faire du menu déroulant un widget cliquable
        self.comboBox.activated.connect(self.clicker)
        
        # Ajout des données dans le menu déroulant
        self.comboBox.addItem('Calzone')
        self.comboBox.addItem('Champignons')
        self.comboBox.addItem('Fromages')
        self.comboBox.addItem('Poivrons')
        
        # Ajout d'autres données par une liste
        my_toppings = ['Jambon', 'Ananas', 'Suppreme']
        self.comboBox.addItems(my_toppings)
        
        # Bouton d'exécution
        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda:self.clicker())
        self.pushButton.setGeometry(QtCore.QRect(600, 110, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Barre de menus
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # Barre de statuts
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        "Noms rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate(
            "MainWindow", 
            "Sélectionner un élément dans le menu déroulant"))
        self.pushButton.setText(_translate("MainWindow", "Sélectionner"))
        
    def clicker(self):
        "Changement du titre selon la pizza selectionnée"
        
        self.label.setText(
            f"Vous avez choisi : {self.comboBox.currentText()}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
