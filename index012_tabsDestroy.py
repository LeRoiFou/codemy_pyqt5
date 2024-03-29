"""
Cours : Tabs With PyQT5 Designer - PyQt5 GUI Thursdays #11
Lien : https://www.youtube.com/watch?v=URsSTw5nUVM

Dans ce programme on apprend à générer des onglets dans l'application QtDesigner et à insérer des images

Tout d'abord aller sur GitBash :
-> accéder à l'environnement virtuel du répertoire où va se situer les fichiers :
source virt/Scripts/activate
-> saisir : designer (pour accéder à l'application QtDesigner)

Widget pour les onglets :
Lorsqu'on est QtDesigner, pour récuper les pages avec les onglets, aller dans le menu à gauche dans la
partie "Containers" et sélectionner Tab Widget. On a plusieurs possibilités pour ce widget : placement
des titres des onglets, forme des titres des onglets...

Insérer une image :
Pour insérer une image avec QtDesigner, sélectionner dans le menu à gauche le widget Label qui se trouve
dans la partie "Display Widgets"
Puis dans le menu à droite dans la partie QLabel, sélectionner la ligne "pixmap" pour charger une image

Dès que la "simulation" sur l'application QtDesigner est terminée, saisir sur Gitbash :
pyuic5 -x nomFichier.ui -o nomFichier.py

En complément du cours précédent, cette fois-ci on intervient sur le fichier .py pour pouvoir supprimer
un onglet du l'application : c'est à l'utilisateur de choisir s'il veut supprimer un onglet -> cette
procédure n'existe pas sur tkinter

Editeur : Laurent REYNAUD
Date : 30-04-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 627)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # onglets
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 891, 581))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        # mettre False ci-après pour ne pas avoir de bug lorsqu'on supprime
        self.tabWidget.setTabBarAutoHide(False) 
        self.tabWidget.setObjectName("tabWidget")

        # onglet 1
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(310, 90, 231, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/LogoBis.png"))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")

        # onglet 2
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 861, 431))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_2, "")

        # onglet 3
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # instructions pour supprimer un onglet de l'application générée à partir de QtDesigner
        tabs = self.tabWidget
        tabs.tabCloseRequested.connect(lambda index:tabs.removeTab(index))

    def retranslateUi(self, MainWindow):
        # textes rattachés auwx widgets

        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Onglet n° 1"))
        self.label_2.setText(_translate("MainWindow", "C\'est le texte de l\'onglet n° 2 !"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Onglet n° 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Onglet n° 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
