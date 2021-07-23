"""
Cours : How To Use The Dial Widget - PyQt5 GUI Thursdays #22
Lien : https://www.youtube.com/watch?v=sHZf729Hwgk

Dans ce cours on a recours à un widget sous la forme d'un bowling
Widget récupéré dans l'application Designer :
Partie 'Input Widgets' -> Dial
On utilise certaines fonctionnalités de ce widget

Editeur : Laurent REYNAUD
Date : 23-07-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        "Configuration des widgets"
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Widget en forme de bowling
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(130, 20, 291, 191))
        self.dial.setObjectName("dial")
        
        # Fonctionnalité du widget dial : position mini et maxi
        # self.dial.setMinimum(10)
        # self.dial.setMaximum(360)
        # self.dial.setRange(100, 200) # autre possibilité avec (min, max)
        
        # Fonctionnalité du widget dial : position par défaut
        # self.dial.setValue(50)
        
        # Fonctionnalité du widget dial : affichage des graduations
        self.dial.setNotchesVisible(True)
        
        # Fonctionnalité du widget dial : affichage de la position
        self.dial.valueChanged.connect(lambda: self.dialer())
        
        # Fonctionnalité du widget dial : couleurs
        self.dial.setStyleSheet('background-color: blue')
        
        # Titre
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 200, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        # Barre de menus
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 26))
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
        self.label.setText(_translate("MainWindow", "Position actuelle : 0"))

    def dialer(self):
        "Affichage de la position du widget dial"
        
        # Récupération de la position actuel du widget dial
        value = self.dial.value()
        # print(value)
        
        # Mise à jour du texte
        self.label.setText(f"Position actuelle : {str(value)}")
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
