"""
Récapitulatif des fonctions natives dans pyqt5

Touches raccourcies :
-> pour tout plier : CTRL + K + 1
-> pour tout déplier : CTRL + K + J

Cours à voir à partir de index010_toolbars&menus

Éditeur : Laurent REYNAUD
Date : 23-05-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class SetText(object):
    """
    La fonction setText() permet de modifier le texte initial
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index006_designer-2
    index008_calculator
    index009_calculator
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # étiquette
        self.my_label = QtWidgets.QLabel(self.centralwidget)
        self.my_label.setGeometry(QtCore.QRect(260, 50, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.my_label.setFont(font)
        self.my_label.setAlignment(QtCore.Qt.AlignCenter)
        self.my_label.setObjectName("my_label")

        # bouton
        self.my_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it())
        self.my_button.setGeometry(QtCore.QRect(310, 210, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.my_button.setFont(font)
        self.my_button.setObjectName("my_button")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.my_label.setText(_translate("MainWindow", "Texte initial"))
        self.my_button.setText(_translate("MainWindow", "Appuies !"))

    def press_it(self):
        
        self.my_label.setText('Texte modifié !')

class Text(object):
    """
    La fonction text() permet de récupérer le texte d'un widget
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index008_calculator
    index009_calculator
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 624)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # étiquette1
        self.my_label1 = QtWidgets.QLabel(self.centralwidget)
        self.my_label1.setGeometry(QtCore.QRect(260, 50, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.my_label1.setFont(font)
        self.my_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.my_label1.setObjectName("my_label1")

        # bouton
        self.my_button = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.press_it())
        self.my_button.setGeometry(QtCore.QRect(310, 210, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.my_button.setFont(font)
        self.my_button.setObjectName("my_button")

        # étiquette2
        self.my_label2 = QtWidgets.QLabel(self.centralwidget)
        self.my_label2.setGeometry(QtCore.QRect(270, 360, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.my_label2.setFont(font)
        self.my_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.my_label2.setObjectName("my_label2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.my_label1.setText(_translate("MainWindow", "Texte étiquette n° 1"))
        self.my_button.setText(_translate("MainWindow", "Appuies !"))
        self.my_label2.setText(_translate("MainWindow", "Texte étiquette n° 2"))

    def press_it(self):
        
        self.my_label2.setText(self.my_label1.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # Liste ci-après des fonctions natives de pyqt5
    # setText = SetText()
    # setText.setupUi(MainWindow)
    text = Text()
    text.setupUi(MainWindow)
    # Fin de la liste ci-avant des fonctions natives de pyqt5
    MainWindow.show()
    sys.exit(app.exec_())
