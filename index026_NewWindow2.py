"""
Si on lance directement ce module, on aura un message d'erreur
informant que l'appel de la méthode setupUi n'a qu'un argument
alors que celle-ci dispose de deux paramètres ('self' non pris en compte)

Mais lorsqu'on lance ce programme à partir du module 
index026_NewWindow1, il n'y a plus de message d'erreurs... magique !
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SecondWindow(object):
    "Seconde fenêtre"
    
    def closeMain(self, main_w):
        "Fermeture de la fenêtre principale"
        
        main_w.hide()
    
    def showMain(self, main_w):
        "Affichage de la fenêtre principale"
        
        main_w.show()
        
    
    def hideSecond(self, second_w):
        "Fermeture de la seconde fenêtre"
        
        second_w.hide()
    
    def setupUi(self, SecondWindow, MainWindow): # Nouvel argument ajouté
        "Configuration des widgets"
        
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(860, 203)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        SecondWindow.setCentralWidget(self.centralwidget)
        
        # Titre
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, -10, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Bouton Fenêtre 1 masquée
        self.pushButtonHideMain = QtWidgets.QPushButton(
            self.centralwidget, 
            clicked=lambda:self.closeMain(MainWindow)) # argument !
        self.pushButtonHideMain.setGeometry(QtCore.QRect(10, 80, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonHideMain.setFont(font)
        self.pushButtonHideMain.setObjectName("pushButtonHideMain")
        
        # Bouton Fenêtre 1 affichée
        self.pushButtonShowMain = QtWidgets.QPushButton(
            self.centralwidget, 
            clicked=lambda:self.showMain(MainWindow)) # argument !
        self.pushButtonShowMain.setGeometry(QtCore.QRect(290, 80, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonShowMain.setFont(font)
        self.pushButtonShowMain.setObjectName("pushButtonShowMain")
        
        # Bouton Masquée cette fenêtre
        self.pushButtonHideCurrent = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda:self.hideSecond(SecondWindow))
        self.pushButtonHideCurrent.setGeometry(QtCore.QRect(570, 80, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonHideCurrent.setFont(font)
        self.pushButtonHideCurrent.setObjectName("pushButtonHideCurrent")
        
        # Barre de menu et de statuts
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        "Textes rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.label.setText(_translate(
            "SecondWindow", "Tapez quelque chose dans l\'autre fenêtre !"))
        self.pushButtonHideMain.setText(
            _translate("SecondWindow", "Fenêtre 1 masquée"))  
        self.pushButtonShowMain.setText(
            _translate("SecondWindow", "Fenêtre 1 affichée"))
        self.pushButtonHideCurrent.setText(
            _translate("SecondWindow", "Masquée cette fenêtre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow) # Il n'y a qu'un seul argument au lieu de deux...
    SecondWindow.show()
    sys.exit(app.exec_())
