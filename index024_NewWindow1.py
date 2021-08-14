"""
Cours : How To Open A Second Window - PyQt5 GUI Thursdays #24
Lien : https://www.youtube.com/watch?v=R5N8TA0KFxc

Dans ce programme on apprend à afficher une nouvelle fenêtre à partir
d'autres modules
Une nouvelle fenêtre = un nouveau module

Éditeur : Laurent REYNAUD
Date : 14-08-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from index024_NewWindow2 import Ui_SecondWindow
from index024_NewWindow3 import Ui_Dialog

class Ui_MainWindow(object):
    
    def openWindow(self):
        "Ouverture d'une nouvelle fenêtre avec le 3ème module"
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
   
#     def openWindow(self):
#         "Ouverture d'une nouvelle fenêtre avec le 2ème module"
        
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_SecondWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()
        
    def setupUi(self, MainWindow):
        "Configuration des widgets"
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 346)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Bouton d'exécution
        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda:self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(160, 100, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        # Menu et barre de statuts
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 681, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        "Textes rattachés aux widgets"
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate(
            "MainWindow", "Ouvrir une nouvelle fenêtre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
