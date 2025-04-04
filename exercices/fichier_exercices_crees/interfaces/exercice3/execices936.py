# 6- Ecrire une fonction actualiser_bouton, qui actualise le texte des boutons de manière à faire apparaitre le X ou le O sur le bouton joué.  
# Cette fonction sera appelée apres le tour du jouer et apres celui du programme. C'est à dire à la fin des fonctions remplir_grille et
# jouer_coup_aleatoire


import sys
from PyQt5 import   QtWidgets, uic
import numpy as np
import random


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
        self.radioButton_o.setChecked(True)
        self.grille = np.full((3, 3), 2, dtype=int)# table de 3 lignes 3 colonnes rempli de 2 (on garde 0 et 1 pour le remplissage)
        
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
            
            
    def remplir_grille(self):

        """
       4-Récuperer les lignes et colonne des boutons cliqués et les visualiser dans un tableau numpy 3 lignes 3 colonnes.
        - Récupérer le signal de chaque bouton cliqué  
        - Identifier la ligne et colonne du bouton à partir de son nom    
        - Verifier si la case est libre (si elle n'a jamais été selectionnée) On verifiera si elle contient un 2  
        - Remplir l'emplacement dans le self.grille par un o si le joueur a choisi 'O' ou un 1 si il achoisi 'X'
        """
        # Récupérer le bouton qui a été cliqué
        sender = self.sender()  
        # Obtenir le nom du bouton
        bouton = sender.objectName()  
    
        # Déterminer la ligne et la colonne à partir du nom du bouton
        ligne = int(bouton[-2])
        colonne = int(bouton[-1])

        # Vérifier si la case est vide (ici on a initialisé le tableau avec des 2)
        if self.grille[ligne][colonne] == 2:
            # Remplissez la case avec la marque du joueur (0 ou 1)
            if self.marque == "X" :
                self.grille[ligne][colonne] = 1            
            else:
                self.grille[ligne][colonne] = 0

        print(self.grille)   
        # Jouer un coup aléatoire pour le programme
        self.jouer_coup_aleatoire()
        print(self.grille)  
        print('---------------------------')
        self.actualiser_bouton()#<===========
        
    def jouer_coup_aleatoire(self):
        """
         5- passer la valeur correspondant à la position dans le tableau numpy à 0 si le joueur a choisi X ou à 1 si le joueur a choisi 0.
        """
        cases_disponibles = [(i, j) for i in range(3) for j in range(3) if self.grille[i][j] == 2]
        if cases_disponibles:
            ligne, colonne = random.choice(cases_disponibles)
            bouton = "self.pushButton_" + str(ligne) + str(colonne)
            print(bouton)
            if self.marque == "X" :
                self.grille[ligne][colonne] = 0  # jouer la marque que n'a pas choisi le joueur    
            else:
                self.grille[ligne][colonne] = 1 
                
            # Mettez à jour l'interface graphique
            self.actualiser_bouton()#<===========
            print("Le programme a joué sur la case ({}, {})".format(ligne, colonne))
        
    def actualiser_bouton(self):#<===========
        """
        6- Actualiser le texte des boutons de manière à faire apparaitre le X ou le O sur le bouton joué
        """
        indices_zero = np.where(self.grille == 0)#<===========
        indices_un = np.where(self.grille == 1)#<===========
    
        self.grille_texte = np.full((3, 3), " ", dtype=str)#<===========
        self.grille_texte[indices_zero] = "O"#<===========
        self.grille_texte[indices_un] = "X"#<===========
        
        self.pushButton_00.setText(self.grille_texte[0][0])#<===========
        self.pushButton_01.setText(self.grille_texte[0][1])#<===========
        self.pushButton_02.setText(self.grille_texte[0][2])#<===========
        self.pushButton_10.setText(self.grille_texte[1][0])#<===========
        self.pushButton_11.setText(self.grille_texte[1][1])#<===========
        self.pushButton_12.setText(self.grille_texte[1][2])#<===========
        self.pushButton_20.setText(self.grille_texte[2][0])#<===========
        self.pushButton_21.setText(self.grille_texte[2][1])#<===========
        self.pushButton_22.setText(self.grille_texte[2][2])#<===========
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

