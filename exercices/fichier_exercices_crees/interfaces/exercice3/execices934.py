# 4- On veut créer une fonction remplir_grille qui permettra de récuperer les lignes et colonne des boutons cliqués et 
# les visualiser dans un tableau numpy 3 lignes 3 colonnes.
# Commencer par connecter l'ensemble des boutons à la fonction remplir_grille.
# Cette fonction doit:
# - Récupérer le signal de chaque bouton cliqué. On utilisera la syntaxe :   
# ```python
# sender = self.sender()
# bouton = sender.objectName()
# ```
# - Identifier la ligne et colonne du bouton à partir de son nom    
# - Verifier si la case est libre (si elle n'a jamais été selectionnée) On verifiera si elle contient un 2  
# - Remplir l'emplacement dans le self.grille par un o si le joueur a choisi 'O' ou un 1 si il achoisi 'X'

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
        self.grille = np.full((3, 3), 2, dtype=int)
        
        # Connexion des radio buttons
        self.radioButton_o.clicked.connect(self.marques)
        self.radioButton_x.clicked.connect(self.marques)
        #connecter les boutons de la grille
        self.pushButton_00.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_01.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_02.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_10.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_11.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_12.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_20.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_21.clicked.connect(self.remplir_grille)#<===========
        self.pushButton_22.clicked.connect(self.remplir_grille)#<===========
               
    def marques(self):
        """
        3- Connecter les boutons radio pour le choix des marques et créer la fonction marques. Cette fonction permettra d'affecter
        'X' ou 'O' à self.marque en fonction du choix du joueur
        """
        if self.radioButton_o.isChecked():
            self.marque = 'O'
            print(self.marque)
            
        if self.radioButton_x.isChecked():
            self.marque = 'X'
            print(self.marque)
            
    def remplir_grille(self):#<===========
        """
        4-Récuperer les lignes et colonne des boutons cliqués et les visualiser dans un tableau numpy 3 lignes 3 colonnes.
        - Récupérer le signal de chaque bouton cliqué  
        - Identifier la ligne et colonne du bouton à partir de son nom    
        - Verifier si la case est libre (si elle n'a jamais été selectionnée) On verifiera si elle contient un 2  
        - Remplir l'emplacement dans le self.grille par un o si le joueur a choisi 'O' ou un 1 si il achoisi 'X'
        """
        # Récupérer le bouton qui a été cliqué
        sender = self.sender()#<===========  
        # Obtenir le nom du bouton
        bouton = sender.objectName()#<===========  
    
        # Déterminer la ligne et la colonne à partir du nom du bouton
        ligne = int(bouton[-2])#<===========
        colonne = int(bouton[-1])#<===========

        # Vérifier si la case est vide (ici on a initialisé le tableau avec des 2)
        if self.grille[ligne][colonne] == 2:#<===========
            # Remplissez la case avec la marque du joueur (0 ou 1)
            if self.marque == "X" :#<===========
                self.grille[ligne][colonne] = 1 #<===========
            else:#<===========
                self.grille[ligne][colonne] = 0#<===========
        print(self.grille)  #<=========== 
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

