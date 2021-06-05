"""
Cours : Using The Statusbar - PyQt5 GUI Thursdays #17
Lien : https://www.youtube.com/watch?v=m_DYnnr8N00

Dans ce programme, on intervient sur la barre d'état située en bas
de la fenêtre principale :
-> affichage d'un message par défaut ;
-> modification et suppression du message ;
-> modification de la taille de police avec QFont

Editeur : Laurent REYNAUD
Date : 05-06-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont # taille de police des widgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """Configuration des widgets"""
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 189)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Bouton 1
        self.my_button1 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.push_1())
        self.my_button1.setGeometry(QtCore.QRect(10, 0, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_button1.setFont(font)
        self.my_button1.setObjectName("my_button1")

        # Bouton 2
        self.my_button2 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.push_2())
        self.my_button2.setGeometry(QtCore.QRect(390, 0, 371, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.my_button2.setFont(font)
        self.my_button2.setObjectName("my_button2")

        # Barre d'état
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Rajout des instructions ci-après pour la barre d'état
        self.statusbar.setFont(QFont("Helvetica", 16))
        self.statusbar.showMessage("Prêt...")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def push_1(self):
        """Méthode permettant d'afficher du texte dans la barre d'état"""
        
        self.statusbar.showMessage("J'ai appuyé sur le bouton !")

    def push_2(self):
        """Méthode permettant de supprimer le texte affiché dans la barre d'état"""
            
        self.statusbar.showMessage("")

    def retranslateUi(self, MainWindow):
        """Textes rattachés auwx widgets"""

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Barre d'état"))
        self.my_button1.setText(_translate("MainWindow", "Afficher"))
        self.my_button2.setText(_translate("MainWindow", "Effacer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
