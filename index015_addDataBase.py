"""
Cours : Using SQLite3 For Our ToDo List App part 2 - PyQt5 GUI Thursdays #15
Lien : https://www.youtube.com/watch?v=4wplGk935r8&list=PLCC34OHNcOtpmCA8s_dpPMvQLyHbvxocY&index=15

Dans ce programme on apprend à générer une liste des choses à faire à partir de l'application QtDesigner

Dans ce programme on a recours au SGBD avec le module sqlite3 pour :
-> créer une base de données
-> afficher les données de cette base dans la zone de liste
-> sauvegarder les données de la zone de liste dans le SGBD
Avec intervention sur les méthodes suivantes :
-> grab_all()
-> save_it()

D'autre part on apprend à créer un nouveau widget 'pop-up':
C'est message d'information que la donnée a été sauvegardée et qui figure dans
la méthode save_it()

Editeur : Laurent REYNAUD
Date : 29-05-2021
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox # pop-up
import sqlite3 # base de données

# création d'une base de données ou connection à celle-ci
conn = sqlite3.connect('database/mylist.db')

# création d'un curseur
c = conn.cursor()

"""création d'une table (langage SQL) au nom de list_item
qui est dans une base de données au nom de todo-list"""
c.execute("""CREATE TABLE if not exists todo_list
    (
    list_item text
    )""")

# sauvegarde des changements
conn.commit()

# fermeture de la connection
conn.close()

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # Méthode de configuration des widgets

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(741, 490)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ligne de champ de saisie
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(10, 20, 721, 41))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")

        # bouton "Ajouter l'enregistrement"
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.add_it())
        self.addItem_pushButton.setGeometry(QtCore.QRect(10, 70, 181, 41))
        self.addItem_pushButton.setObjectName("addItem_pushButton")

        # bouton "Effacer l'enregistrement"
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.delete_it())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(190, 70, 181, 41))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")

        # bouton "Supprimer tout"
        self.clearAll_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.clear_it())
        self.clearAll_pushButton.setGeometry(QtCore.QRect(370, 70, 181, 41))
        self.clearAll_pushButton.setObjectName("clearAll_pushButton")
        
        # bouton "Sauvegarder"
        self.save_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.save_it())
        self.save_pushButton.setGeometry(QtCore.QRect(550, 70, 181, 41))
        self.save_pushButton.setObjectName("save_pushButton")

        # zone de liste des données
        self.mylist_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.mylist_listWidget.setGeometry(QtCore.QRect(10, 120, 721, 321))
        self.mylist_listWidget.setObjectName("mylist_listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 741, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # affichage des données issues de la base de données mylist.db
        self.grab_all()

    def grab_all(self):
        # méthode permettant d'afficher les données issues du SGBD

        # création d'une base de données ou connection à celle-ci
        conn = sqlite3.connect('database/mylist.db')

        # création d'un curseur
        c = conn.cursor()

        # récupération des données dans le SGBD (langage SQL)
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # sauvegarde des changements
        conn.commit()

        # fermeture de la connection
        conn.close()

        # boucle pour l'affichage des données dans la zone de liste
        for record in records:
            # print(record)
            self.mylist_listWidget.addItem(str(record[0]))

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

    def save_it(self):
        # Méthode pour sauvegarder les données dans un SGBD

         # création d'une base de données ou connection à celle-ci
        conn = sqlite3.connect('database/mylist.db')

        # création d'un curseur
        c = conn.cursor()

        """remplacement de toutes les données dans le SGBD (langage SQL)
        à défaut les données vont se cumuler dans le SGBD"""
        c.execute('DELETE FROM todo_list;',)

        # création d'une liste pour récupérer les données
        items = []

        # boucle pour récupérer les saisies dans la zone de liste de données
        for index in range(self.mylist_listWidget.count()):
            items.append(self.mylist_listWidget.item(index))
        
         # ajout des données dans la table (langage SQL)
        for item in items:
            # print(item.text())    
            c.execute('INSERT INTO todo_list VALUES (:item)',
                {
                'item': item.text(),
                }
                )

        # sauvegarde des changements
        conn.commit()

        # fermeture de la connection
        conn.close()

        # message d'information
        msg = QMessageBox()

        # titre de la fenêtre de message d'information
        msg.setWindowTitle("Donnée sauvegardée !")

        # texte principal de la fenêtre de message d'information
        msg.setText("Votre liste de données a été sauvegardée !")

        # icône de message d'information
        msg.setIcon(QMessageBox.Information)

        # exécution du message d'information
        x = msg.exec_()


    def retranslateUi(self, MainWindow):
        # Méthode de saisie dans les widgets

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Liste à traiter"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Ajouter l\'enregistrement"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Effacer l\'enregistrement"))
        self.clearAll_pushButton.setText(_translate("MainWindow", "Supprimer tout"))
        self.save_pushButton.setText(_translate("MainWindow", "Sauvegarder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
