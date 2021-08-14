from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        "Configuration des widgets"
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(575, 122)
        
        # Etiquette
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 541, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        # Textes rattachés aux widgets
        
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate(
            "Dialog", "Tapez quelque chose dans l\'autre fenêtre !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
