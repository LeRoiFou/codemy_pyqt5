"""
Cours : Hide First Window From Second Window - PyQt5 GUI Thursdays #26
Lien : https://www.youtube.com/watch?v=OmZ-WUDr4JQ

Dans ce programme en complément du cours précédent, on masque / affiche
la fenêtre principale et on peut également masquer la seconde fenêtre

À la différence des programmes précédents, on effectue une instruction
aussi bien de ce module vers l'autre module qu'inversement.

Pour ce module on appelle l'autre fichier avec l'instruction suivante :
from index026_NewWindow2 import Ui_SecondWindow
Alors que pour l'autre module, on ne fait pas d'import mais on paramètre
les méthodes grâce à la programmation fonctionnelle lambda

Editeur : Laurent REYNAUD
Date : 20-08-21
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from index026_NewWindow2 import Ui_SecondWindow

class Ui_MainWindow(object):
    "Fenêtre principale"
    
    def open_window(self):
        "Ouverture de la 2ème fenêtre"
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window, MainWindow) # Nouvel argument ajouté
        self.window.show()
    
    def clicker(self):
        "Affichage dans la 2ème fenêtre du texte saisi dans la 1ère fenêtre"
        
        # Affichage préalable de la 2ème fenêtre
        self.open_window()
        
        # Assignation du texte affiché dans la zone de saisie
        thing = self.lineEdit.text()
        
        # Récupération de l'attribut 'label' dans le 2ème module
        self.ui.label.setText(thing)
    
    def setupUi(self, MainWindow):
        "Configuration des widgets"
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 483)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Zone de saisie
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 601, 261))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        
        # Bouton Soummetre
        self.pushButtonSubmit = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda:self.clicker())
        self.pushButtonSubmit.setGeometry(QtCore.QRect(10, 280, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonSubmit.setFont(font)
        self.pushButtonSubmit.setObjectName("pushButtonSubmit")
        
        # Bouton Ouvrir une nouvelle fenêtre
        self.pushButtonNewWindow = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda:self.open_window())
        self.pushButtonNewWindow.setGeometry(QtCore.QRect(10, 360, 601, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButtonNewWindow.setFont(font)
        self.pushButtonNewWindow.setObjectName("pushButtonNewWindow")
        
        # Barre de menu et barre de statuts
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 627, 26))
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
        self.pushButtonSubmit.setText(_translate("MainWindow", "Soumettre"))
        self.pushButtonNewWindow.setText(_translate("MainWindow", "Ouvrir une nouvelle fenêtre"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
