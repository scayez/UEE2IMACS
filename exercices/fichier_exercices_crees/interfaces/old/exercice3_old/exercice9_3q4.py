import sys
from PyQt5 import   QtWidgets, uic
import numpy as np


qtCreatorFile = "exercice9_3.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #initialisations des variables
        self.resultats = np.zeros((0, 2), dtype=int)
        self.marque = 'O'
        # table de 3 lignes 3 colonnes rempli de 2 ( 0 et 1 indiqueront les O et les X)
        self.grille = np.full((3, 3), 2, dtype=int)#<===========
        # Connecter les radio buttons
        self.radioButton_o.clicked.connect(self.marques)
        self.radioButton_x.clicked.connect(self.marques)
        
        #connecter les boutons de la grille
        self.pushButton_00.clicked.connect(self.remplir_grille)
        self.pushButton_01.clicked.connect(self.remplir_grille)
        self.pushButton_02.clicked.connect(self.remplir_grille)
        self.pushButton_10.clicked.connect(self.remplir_grille)
        self.pushButton_11.clicked.connect(self.remplir_grille)
        self.pushButton_12.clicked.connect(self.remplir_grille)
        self.pushButton_20.clicked.connect(self.remplir_grille)
        self.pushButton_21.clicked.connect(self.remplir_grille)
        self.pushButton_22.clicked.connect(self.remplir_grille)
        
        
    def marques(self):
        """Choix de la marque du joueur"""
        if self.radioButton_o.isChecked():
            self.marque = 'O'
            print(self.marque)
            
        if self.radioButton_x.isChecked():
            self.marque = 'X'
            print(self.marque)
            
            
    def remplir_grille(self):
        print('grille')
        sender = self.sender()  # Récupérez le bouton qui a été cliqué
        bouton = sender.objectName()  # Obtenez le nom du bouton
    
        # Déterminez la ligne et la colonne à partir du nom du bouton
        ligne = int(bouton[-2])
        colonne = int(bouton[-1])

        # Vérifiez si la case est vide (ici on a initialisé le tableau avec des 2)
        if self.grille[ligne][colonne] == 2:
            # Remplissez la case avec la marque du joueur (0 ou 1)
            if self.marque == "X" :
                self.grille[ligne][colonne] = 1 
            else:
                self.grille[ligne][colonne] = 0
            
            # self.grille[ligne][colonne] = 1 if self.marque == "X" else 0
        print(self.grille)   
        
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())