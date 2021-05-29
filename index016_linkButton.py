"""
Cours : Using The Command Link Button - PyQt5 GUI Thursdays #16
Lien : https://www.youtube.com/watch?v=49PJrKsSZ6c&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=16

Dans ce programme on apprend à augmenter le compteur de + 1 à chaque fois qu'on appuye sur le bouton

Dans l'application QtDesigner, le widget pour le bouton avec une "->" c'est :
Command Link Button dans la partie Buttons

Editeur : Laurent REYNAUD
Date : 29-05-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(692, 135)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # bouton d'exécution + assignation d'un compteur
        self.count = 0     
        self.next_command = QtWidgets.QCommandLinkButton(self.centralwidget, clicked=lambda:self.increment())
        self.next_command.setGeometry(QtCore.QRect(10, 20, 251, 48))
        self.next_command.setObjectName("next_command")

        # compteur à afficher
        self.next_label = QtWidgets.QLabel(self.centralwidget)
        self.next_label.setGeometry(QtCore.QRect(430, 10, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.next_label.setFont(font)
        self.next_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.next_label.setObjectName("next_label")
     
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def increment(self):
        # méthode permettant de modifier le texte affiché en incrémentant de 1
        
        # incrémentationd de 1
        self.count += 1

        # modification du texte affiché
        self.next_label.setText(str(self.count))

    def retranslateUi(self, MainWindow):
        # textes rattachés auwx widgets

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_command.setText(_translate("MainWindow", "Augmenter le compteur"))
        self.next_label.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
