"""
Cours : ToDo List GUI App - PyQt5 GUI Thursdays #13
Lien : https://www.youtube.com/watch?v=EFKI9bu4lrY&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=13

Dans ce programme on apprend à générer une liste des choses à faire à partir de l'application QtDesigner

Editeur : Laurent REYNAUD
Date : 08-05-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # Méthode de configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # bouton "Ajouter l'enregistrement"
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 70, 181, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        
        # ligne de champ de saisie
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(10, 20, 541, 41))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        
        # zone de liste des données
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 120, 541, 321))
        self.mylist_listWidget.setObjectName("mylist_listView")
        
        # bouton "Effacer l'enregistrement"
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(190, 70, 181, 41))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
       
        # bouton "Supprimer tout"
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(370, 70, 181, 41))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def add_it(self):
        # Méthode pour ajouter une donnée à partir du bouton "Ajouter l'enregistrement"

        # récupération du texte affiché dans la ligne de saisie
        item = self.addItem_lineEdit.text()

        # ajout du texte récupéré dans la zone de liste
        self.mylist_listWidget.addItem(item)

        # le texte affiché dans la ligne de saisie est effacé
        self.addItem_lineEdit.setText("")

    def delete_it(self):
        # Méthode pour effacer une donnée à partir du bouton "Effacer l'enregistrement"

        # récupération de la ligne sélectionnée dans la zone de liste
        clicked = self.mylist_listWidget.currentRow()
        # affiche dans la console le n° du composant en partant de 0 comme une liste
        # print(clicked) 
        # affiche dans la ligne de saisie le n° du composant en partant de 0 comme une liste
        # self.addItem_lineEdit.setText(str(clicked))

        # récupérer la ligne sélectionnée selon son n° de composant et suppression
        self.mylist_listWidget.takeItem(clicked)


    def clear_it(self):
        # Méthode pour supprimer toutes les données à partir du bouton "Supprimer tout"

       self.mylist_listWidget.clear()

    def retranslateUi(self, MainWindow):
        # Méthode de saisie dans les widgets

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Liste à traiter"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Ajouter l\'enregistrement"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Effacer l\'enregistrement"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Supprimer tout"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
