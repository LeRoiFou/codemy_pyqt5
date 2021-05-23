"""
PyQt5 - Codemy.com #006 : PyQT5 Designer Drag and Drop GUI - PyQt5 GUI Thursdays #6
Lien : https://www.youtube.com/watch?v=5K__zwBj_nY

Dans ce programme on apprend à utiliser QtDesigner qui permet une mise en format des widgets
Package installé dans le répertoire venv (environnement virtuel) : PyQt5Designer

En complément du précédent programme, cette-fois on affectue une exécution au widget Button

Éditeur : Laurent REYNAUD
Date : 01-03-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # étiquette
        self.my_label = QtWidgets.QLabel(self.centralwidget)
        self.my_label.setGeometry(QtCore.QRect(40, 60, 691, 191))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.my_label.setFont(font)
        self.my_label.setObjectName("my_label")

        # bouton
        self.my_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it())  # rajout fonction
        self.my_button.setGeometry(QtCore.QRect(20, 360, 771, 171))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.my_button.setFont(font)
        self.my_button.setObjectName("my_button")

        # barre de menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self):
        # Méthode permettant de changer le texte après avoir appuyé sur le bouton
        
        self.my_label.setText('Tu as appuyé sur le bouton !')

    def retranslateUi(self, MainWindow):
        # textes rattachés aux widgets

        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.my_label.setText(_translate("MainWindow", "Mon 1er QT Designer ;)"))
        self.my_button.setText(_translate("MainWindow", "Appuie !"))


if __name__ == "__main__":
    import sys  # module supplémentaire à rajouter lorsqu'on utilise QtDesigner qui est un outil externe

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
