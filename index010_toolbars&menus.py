"""
PyQt5 - Codemy.com #10 : Adding Toolbars and Menus with PyQt5 Designer - PyQt5 GUI Thursdays #10
Lien : https://www.youtube.com/watch?v=IWPIP_V_sFY

Dans ce programme on apprend à mettre en place un menu et une barre d'outils dans l'application QtDesigner

Lorqu'on ouvre l'application QtDesigner, dont l'exécutable se trouve dans le chemin suivant :
C:/Users/LRCOM/pythonProjects/codemy_pyqt5/virt/Lib/site-packages/QtDesigner
À la création sélectionner Main Window
En haut de la nouvelle fenêtre saisir le menu souhaité

Pour ajouter une barre d'outils, clique droit sur la fenêtre principale puis sélectionner : 
Ajouter une barre d'outils

Pour mettre des icônes, il y a un site dédié qui comprend + de 3000 icônes :
https://p.yusukekamiyamane.com/
Télécharger le dossier à dézipper comprenant tous les icônes et mettre le dossier dans le même répertoire que le fichier .py

Pour rattacher une icône à un menu / une barre d'outils, aller dans la fenêtre en bas à droite de l'application :
Éditeur d'actions

Pour rappel, pour avoir une prévisualisation du design sur QtDesigner : touches CTRL + R
Et pour générer le script à partir de QtDesigner sur GitBash dans le répertoire où se trouve le fichier .py à compléter :
pyuic5 -x nomFichier.ui -o nomFichier.py

Éditeur : Laurent REYNAUD
Date : 26-03-2021
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

        # barre de menu
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        # menu 'Fichier'
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")

        self.actionOuvrir = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/fugue-icons-3.5.6/icons/book-open-text.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOuvrir.setIcon(icon)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.menuFichier.addAction(self.actionOuvrir)
        self.toolBar.addAction(self.actionOuvrir)

        self.actionJnouveau = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/fugue-icons-3.5.6/icons/blue-document--plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJnouveau.setIcon(icon1)
        self.actionJnouveau.setObjectName("actionJnouveau")
        self.menuFichier.addAction(self.actionJnouveau)
        self.toolBar.addAction(self.actionJnouveau)

        self.actionEnregistrer = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer.setObjectName("actionEnregistrer")
        self.menuFichier.addAction(self.actionEnregistrer)

        self.actionEnregistrer_sous = QtWidgets.QAction(MainWindow)
        self.actionEnregistrer_sous.setObjectName("actionEnregistrer_sous")
        self.actionCouper = QtWidgets.QAction(MainWindow)
        self.menuFichier.addAction(self.actionEnregistrer_sous)

        # séparateur
        self.menuFichier.addSeparator()
        
        self.actionQuitter = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/fugue-icons-3.5.6/icons-shadowless/hand-finger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuitter.setIcon(icon3)
        self.actionQuitter.setObjectName("actionQuitter")
        self.menuFichier.addAction(self.actionQuitter)
        self.toolBar.addAction(self.actionQuitter)

        self.menubar.addAction(self.menuFichier.menuAction())

        # menu 'Edition'
        self.menuEdition = QtWidgets.QMenu(self.menubar)
        self.menuEdition.setObjectName("menuEdition")

        self.actionCouper = QtWidgets.QAction(MainWindow)
        self.actionCouper.setObjectName("actionCouper")
        self.menuEdition.addAction(self.actionCouper)

        self.actionCopier = QtWidgets.QAction(MainWindow)
        self.actionCopier.setObjectName("actionCopier")
        self.menuEdition.addAction(self.actionCopier)

        self.actionColler = QtWidgets.QAction(MainWindow)
        self.actionColler.setObjectName("actionColler")
        self.menuEdition.addAction(self.actionColler)

        self.actionRechercher = QtWidgets.QAction(MainWindow)
        self.actionRechercher.setObjectName("actionRechercher")
        self.menuEdition.addAction(self.actionRechercher)

        self.actionRemplacer = QtWidgets.QAction(MainWindow)
        self.actionRemplacer.setObjectName("actionRemplacer")
        self.menuEdition.addAction(self.actionRemplacer)

        self.menubar.addAction(self.menuEdition.menuAction())

        # menu 'Aide'
        self.menuAide = QtWidgets.QMenu(self.menubar)
        self.menuAide.setObjectName("menuAide")

        self.action_propos = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/fugue-icons-3.5.6/icons/question.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_propos.setIcon(icon2)
        self.action_propos.setObjectName("action_propos")
        self.menuAide.addAction(self.action_propos)
             
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # textes rattachés aux widgets

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuEdition.setTitle(_translate("MainWindow", "Edition"))
        self.menuAide.setTitle(_translate("MainWindow", "Aide"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionJnouveau.setText(_translate("MainWindow", "Nouveau"))
        self.actionEnregistrer.setText(_translate("MainWindow", "Enregistrer"))
        self.actionEnregistrer_sous.setText(_translate("MainWindow", "Enregistrer sous"))
        self.actionCouper.setText(_translate("MainWindow", "Couper"))
        self.actionCopier.setText(_translate("MainWindow", "Copier"))
        self.actionColler.setText(_translate("MainWindow", "Coller"))
        self.action_propos.setText(_translate("MainWindow", "À propos"))
        self.actionRechercher.setText(_translate("MainWindow", "Rechercher"))
        self.actionRemplacer.setText(_translate("MainWindow", "Remplacer"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionQuitter.setToolTip(_translate("MainWindow", "Quitter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
