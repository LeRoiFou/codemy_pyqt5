# PyQt5 - Codemy.com #009 : Build Calculator Functionality - PyQt5 GUI Thursdays #9
# Lien : https://www.youtube.com/watch?v=YEOOcrm5ulA

# Dans ce programme on apprend à créer une calculatrice en configurant sa mise en forme à l'aide de QtDesigner

# Dans ce chapitre on apprend :
# -> à effacer le dernier caractère saisi (fonction remove_it())
# -> à afficher une seule décimale (fonction dot_it() à compléter au prochain chapitre)
# -> à afficher le signe '-' lorsqu'on appuye sur le bouton '+/-' avec la fonction plus_minus_it()
# -> à afficher le résultat avec la fonction math_it()

# Le commentaire ci-dessous est généré avec le script après avoir enregistré le fichier .ui de QtDesigner et avoir
# saisi sur GitBash : pyuic5 -x 008_calculator.ui -o 008_calculator.py

# Éditeur : Laurent REYNAUD
# Date : 20-03-2021


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '008_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)

        # affichage écran de la calculatrice
        self.outputLabel = QtWidgets.QLabel(MainWindow)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        # bouton '%'
        self.percentButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")

        # bouton 'C'
        self.cButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")

        # bouton '<<'
        self.arrowButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.remove_it())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")

        # bouton '/'
        self.divideButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")

        # bouton '7'
        self.sevenButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")

        # bouton '8'
        self.eightButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")

        # bouton '9'
        self.nineButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")

        # bouton '*'
        self.multiplyButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")

        # bouton '4'
        self.fourButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")

        # bouton '5'
        self.fiveButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")

        # bouton '6'
        self.sixButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")

        # bouton '-'
        self.minusButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")

        # bouton '1'
        self.oneButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")

        # bouton '2'
        self.twoButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")

        # bouton '3'
        self.threeButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")

        # bouton '+'
        self.addButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")

        # bouton '+/-'
        self.plusminusButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.plus_minus_it())
        self.plusminusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusminusButton.setFont(font)
        self.plusminusButton.setObjectName("plusminusButton")

        # bouton '0'
        self.zeroButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")

        # bouton '.'
        self.decimalButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.dot_it())
        self.decimalButton.setGeometry(QtCore.QRect(190, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")

        # bouton '='
        self.equalButton = QtWidgets.QPushButton(MainWindow, clicked= lambda: self.math_it())
        self.equalButton.setGeometry(QtCore.QRect(275, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def remove_it(self):
        """méthode permettant d'effacer le dernier caractère à chaque fois 
        qu'on appuye sur le bouton '<<'"""

        # assignation du widget écran de la calculatrice qui est une str
        screen = self.outputLabel.text()

        # assignation de tous les caractères saisis sauf le dernier caractère
        screen = screen[:-1]

        # affichage à l'écrant de tous les caractères sauf le dernier caractère saisi
        self.outputLabel.setText(screen)

    def math_it(self):
        # méthode pour faire les calculs

        # assignation du widget écran de la calculatrice qui est une str
        screen = self.outputLabel.text()

        try:
            """assignation de la str 'screen' en int qui permet de faire des additions, soustractions...
            qui restitue le resultat en float (c'est fou !!!)"""
            answer = eval(screen)

            # affichage du résultat converti en str pour qu'il puisse être affiché
            self.outputLabel.setText(str(answer))
        except:
            # affichage de l'erreur de saisie
            self.outputLabel.setText("ERREUR")



    def plus_minus_it(self):
        # méthode permettant d'afficher le signe '+' ou le signe '-' avec la touche '+/-'

        # assignation du widget écran de la calculatrice qui est une str
        screen = self.outputLabel.text()

        # si le signe '-' est à l'écran
        if "-" in screen:
            # supprimer le signe '-'
            self.outputLabel.setText(screen.replace("-", ""))
        else:
            # sinon concaténer les chiffres saisis précédés du signe '-'
            self.outputLabel.setText(f"-{screen}")

    def dot_it(self):
        # méthode permettant de saisir qu'une seule fois la décimale '.'

        # assignation du widget écran de la calculatrice qui est une str
        screen = self.outputLabel.text()

        # si le dernier caractère est une décimale
        if screen[-1] == ".":
            pass
        else:
            # concaténer les chiffres saisis avec la décimale '.'
            self.outputLabel.setText(f"{screen}.")

    def press_it(self, pressed):
        # méthode permettant d'afficher sur la calculatrice ce que l'on saisit
        
        # si on appuye sur la touche 'C'
        if pressed == "C":  
            # affichage du chiffre 0
            self.outputLabel.setText("0")  
        else:
            # sinon si le chiffre '0' est déjà affiché
            if self.outputLabel.text() == '0': 
                # supprimer ce chiffre 0
                self.outputLabel.setText("") 
            # concaténer les chiffres saisis
            self.outputLabel.setText(f"{self.outputLabel.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        # textes rattachés aux widgets

        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculatrice"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.equalButton.setText(_translate("MainWindow", "="))
        self.plusminusButton.setText(_translate("MainWindow", "+/-"))
        self.zeroButton.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
