"""
Récapitulatif des fonctions natives dans pyqt5

Touches raccourcies :
-> pour tout plier : CTRL + K + 1
-> pour tout déplier : CTRL + K + J

Éditeur : Laurent REYNAUD
Date : 23-05-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets

class Modele(object):
    """
    La fonction count() permet de ...
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Effacer'
        self.buttonRemove = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.remove_it())
        self.buttonRemove.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setObjectName("buttonRemove")

        # bouton 'Supprimer tout'
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clear_it())
        self.buttonDelete.setGeometry(QtCore.QRect(330, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setObjectName("buttonDelete")

        # bouton 'Sauvegarder'
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.save_it())
        self.buttonSave.setGeometry(QtCore.QRect(490, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonRemove.setText(_translate("MainWindow", "Effacer"))
        self.buttonDelete.setText(_translate("MainWindow", "Supprimer tout"))
        self.buttonSave.setText(_translate("MainWindow", "Sauvegarder"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def remove_it(self):
        # méthode pour effacer la donnée de la ligne sélectionnée dans la zone de liste

        # récupération du n° de composant (componant) de la ligne sélectionnée dans la zone de liste
        componant_number = self.myList.currentRow()

        # récupération du n° de composant sélectionné et suppression de la ligne concernée
        self.myList.takeItem(componant_number)

    def clear_it(self):
        # méthode pour tout supprimer dans la zone de liste

        self.myList.clear()

    def save_it(self):

        test = self.myList.count()
        print(test)

class AddItem(object):
    """
    La fonction addItem() permet d'ajouter des données dans un widget
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

class Clear(object):
    """
    La fonction clear() permet de tout supprimer dans le widget
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Supprimer tout'
        self.buttonDelete = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clear_it())
        self.buttonDelete.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonDelete.setFont(font)
        self.buttonDelete.setObjectName("buttonDelete")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonDelete.setText(_translate("MainWindow", "Supprimer tout"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def clear_it(self):
        # méthode pour tout supprimer dans la zone de liste

        self.myList.clear()

class Count(object):
    """
    La fonction count() permet de compter le nombre de composants dans un widget
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Compter'
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.count_it())
        self.buttonSave.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonSave.setText(_translate("MainWindow", "Compter"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def count_it(self):
        # méthode permettant de compter le nombre de composants dans la zone de liste

        # nombre de composants dans la liste
        my_count = self.myList.count()
        
        # affichage du nombre de composants dans la ligne de saisie
        self.myLineEdit.setText(f"Il y a {my_count} composants dans la zone de liste")

class CurrentRow(object):
    """
    La fonction currentRow() permet de récupérer le n° de composant de la ligne sélectionnée
    du widget concerné
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Effacer'
        self.buttonRemove = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.remove_it())
        self.buttonRemove.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setObjectName("buttonRemove")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonRemove.setText(_translate("MainWindow", "Effacer"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def remove_it(self):
        # méthode pour effacer la donnée de la ligne sélectionnée dans la zone de liste

        # récupération du n° de composant (componant) de la ligne sélectionnée dans la zone de liste
        componant_number = self.myList.currentRow()

        # récupération du n° de composant sélectionné et suppression de la ligne concernée
        self.myList.takeItem(componant_number)

class Item(object):
    """
    La fonction item() est utilisée pour le widget de zone de liste et permet de récupérer
    le texte de chaque ligne présente dans la zone de liste
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Récupérer'
        self.buttonSave = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.recover_it())
        self.buttonSave.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonSave.setFont(font)
        self.buttonSave.setObjectName("buttonSave")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonSave.setText(_translate("MainWindow", "Récupérer"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def recover_it(self):
        # méthode pour récupérer les données figurant dans la zone de liste

        # création d'une liste pour récupérer les données
        items = []

        # boucle pour récupérer les saisies dans la zone de liste de données
        print("Affichage de l'objet widget 'myList'")
        for index in range(self.myList.count()):
            items.append(self.myList.item(index))
            print(self.myList.item(index))
        print('')
        
        # affichage des données de la liste dans la console en recourant à une boucle
        # car chaque composant de la liste est un objet
        print("Affichage de chaque donnée dans la zone de liste")
        for item in items:
            print(item.text())

class SetText(object):
    """
    La fonction setText() permet de modifier le texte initial
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index006_designer-2
    index008_calculator
    index009_calculator
    index013_todoList
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

class TakeItem(object):
    """
    La fonction takeItem() permet de récupérer le n° de composant concerné et de supprimer
    la donnée (texte, chiffre...) affectée à ce n° de composant
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index013_todoList
    """

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(641, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de saisie
        self.myLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.myLineEdit.setGeometry(QtCore.QRect(10, 10, 621, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myLineEdit.setFont(font)
        self.myLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.myLineEdit.setObjectName("myLineEdit")

        # bouton 'Ajouter'
        self.buttonAdd = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.add_it())
        self.buttonAdd.setGeometry(QtCore.QRect(10, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonAdd.setFont(font)
        self.buttonAdd.setObjectName("buttonAdd")

        # bouton 'Effacer'
        self.buttonRemove = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.remove_it())
        self.buttonRemove.setGeometry(QtCore.QRect(170, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.buttonRemove.setFont(font)
        self.buttonRemove.setObjectName("buttonRemove")

        # zone de liste
        self.myList = QtWidgets.QListWidget(self.centralwidget)
        self.myList.setGeometry(QtCore.QRect(10, 140, 621, 301))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.myList.setFont(font)
        self.myList.setObjectName("myList")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 641, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Récapitulatif"))
        self.buttonAdd.setText(_translate("MainWindow", "Ajouter"))
        self.buttonRemove.setText(_translate("MainWindow", "Effacer"))

    def add_it(self):
        # méthode pour ajouter le texte de la ligne de saisie dans la zone de liste

        # récupération du texte affiché dans la ligne de saisie
        text = self.myLineEdit.text()
       
        # ajout dans la zone de liste
        self.myList.addItem(text)

        # texte affiché dans la ligne de saisie effacé
        self.myLineEdit.setText("")

    def remove_it(self):
        # méthode pour effacer la donnée de la ligne sélectionnée dans la zone de liste

        # récupération du n° de composant (componant) de la ligne sélectionnée dans la zone de liste
        componant_number = self.myList.currentRow()

        # récupération du n° de composant sélectionné et suppression de la ligne concernée
        self.myList.takeItem(componant_number)

class Text(object):
    """
    La fonction text() permet de récupérer le texte d'un widget
    Fonction retrouvée dans les cours suivants dans codemy_pyqt5:
    index008_calculator
    index009_calculator
    index013_todoList
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
    # addItem = AddItem()
    # addItem.setupUi(MainWindow)
    # clear = Clear()
    # clear.setupUi(MainWindow)
    # count = Count()
    # count.setupUi(MainWindow)
    # currentRow = CurrentRow()
    # currentRow.setupUi(MainWindow)
    # item = Item()
    # item.setupUi(MainWindow)
    # setText = SetText()
    # setText.setupUi(MainWindow)
    # takeItem = TakeItem()
    # takeItem.setupUi(MainWindow)
    # text = Text()
    # text.setupUi(MainWindow)
    # Fin de la liste ci-avant des fonctions natives de pyqt5
    MainWindow.show()
    sys.exit(app.exec_())
