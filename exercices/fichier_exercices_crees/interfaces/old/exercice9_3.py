# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 06:52:41 2024

@author: cayez
"""

import sys
from PyQt5 import   QtWidgets, uic
import numpy as np
import random
from PyQt5.QtWidgets import QApplication, QMessageBox


qtCreatorFile = "exercice9_3.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        
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
        
        self.pushButton_rejouer.clicked.connect(self.initialiser)
        
        
        
    
        
        
        #remettre les grilles à zero
        self.initialiser()
        
        
    def marques(self):
        """Choix de la marque du joueur"""
        if self.radioButton_o.isChecked():
            self.marque = 'O'
          
            
        if self.radioButton_x.isChecked():
            self.marque = 'X'
        
            
            
    def remplir_grille(self):

   
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

              
            
        
  
        # Jouez un coup aléatoire pour le programme
        
        self.jouer_coup_aleatoire()
  
   
        self.actualiser_bouton()
        
        self.verif_gagnant() 
        
    def jouer_coup_aleatoire(self):
        """Fonction pour jouer un coup aléatoire pour le programme"""
        cases_disponibles = [(i, j) for i in range(3) for j in range(3) if self.grille[i][j] == 2]
        if cases_disponibles:
            ligne, colonne = random.choice(cases_disponibles)
            
      
            # bouton = "pushButton_" + str(ligne) + str(colonne)
            # bouton = "self.pushButton_" + str(ligne) + str(colonne)
           
            if self.marque == "X" :
                self.grille[ligne][colonne] = 0  # jouer la marque que n'a pas choisi le joueur


               
            else:
                self.grille[ligne][colonne] = 1 

               
            # Mettez à jour l'interface graphique ici
            self.actualiser_bouton()
            
            
        
    def actualiser_bouton(self):
        
        indices_zero = np.where(self.grille == 0)
        indices_un = np.where(self.grille == 1)
        # indices_deux = np.where(self.grille == 2)
    
        self.grille_texte = np.full((3, 3), " ", dtype=str)
        self.grille_texte[indices_zero] = "O"
        self.grille_texte[indices_un] = "X"
        
        self.pushButton_00.setText(self.grille_texte[0][0])
        self.pushButton_01.setText(self.grille_texte[0][1])
        self.pushButton_02.setText(self.grille_texte[0][2])
        self.pushButton_10.setText(self.grille_texte[1][0])
        self.pushButton_11.setText(self.grille_texte[1][1])
        self.pushButton_12.setText(self.grille_texte[1][2])
        self.pushButton_20.setText(self.grille_texte[2][0])
        self.pushButton_21.setText(self.grille_texte[2][1])
        self.pushButton_22.setText(self.grille_texte[2][2])
        
        
 
    def verif_gagnant(self):
        # Vérification des lignes et colonnes
  
        if self.marque == 'O':
            for i in range(3):
                if np.all(self.grille[:, i] == 0) or np.all(self.grille[i, :] == 0):
                    print('2 points joueur') 
                    self.afficher_message('Joueur gagne', '2 points joueur')
            if np.all(np.diag(self.grille) == 0) or np.all(np.diag(np.fliplr(self.grille)) == 0):
                print('2 points joueur')
                self.afficher_message('Joueur gagne', '2 points joueur')
        for i in range(3):
            if np.all(self.grille[:, i] == 1) or np.all(self.grille[i, :] == 1):
                print('2 points programme') 
                self.afficher_message('Programme gagne', '2 points programme')                
        if np.all(np.diag(self.grille) == 1) or np.all(np.diag(np.fliplr(self.grille)) ==1):
            print('2 points programme') 
            self.afficher_message('Programme gagne', '2 points programme')            
                
                
        
        if self.marque == 'X':
             for i in range(3):
                 if np.all(self.grille[:, i] == 1) or np.all(self.grille[i, :] == 1):
                     print('2 points joueur')  
                     
                     self.afficher_message('Joueur gagne', '2 points joueur')
             if np.all(np.diag(self.grille) == 1) or np.all(np.diag(np.fliplr(self.grille)) ==1):
                 print('2 points joueur') 
                 self.afficher_message('Joueur gagne', '2 points joueur')
                
     
             for i in range(3):
                 if np.all(self.grille[:, i] == 0) or np.all(self.grille[i, :] == 0):
                     print('2 points programme')
                     self.afficher_message('Programme gagne', '2 points programme')
             if np.all(np.diag(self.grille) == 0) or np.all(np.diag(np.fliplr(self.grille)) == 0):
                 print('2 points programme')
                 self.afficher_message('Programme gagne', '2 points programme')
                
                
    def initialiser(self):
        
        #initialisations des variables
        self.resultats = np.zeros((0, 2), dtype=int)
        self.marque = 'O'
        self.radioButton_o.setChecked(True)
        self.grille = np.full((3, 3), 2, dtype=int)# table de 3 lignes 3 colonnes rempli de 2 (on garde 0 et 1 pour le remplissage)
        
        # efffacer le texte des boutons
        self.pushButton_00.setText(' ')
        self.pushButton_01.setText(' ')
        self.pushButton_02.setText(' ')
        self.pushButton_10.setText(' ')
        self.pushButton_11.setText(' ')
        self.pushButton_12.setText(' ')
        self.pushButton_20.setText(' ')
        self.pushButton_21.setText(' ')
        self.pushButton_22.setText(' ')
                
    def afficher_message(self, titre, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(titre)
        msg_box.setText(message)
        msg_box.exec_()
        #la partie est finie, on initialise
        self.initialiser()   

    # def compter_points(self):
    #     if self.vainqueur == 'joueur':
    #         print('2 points joueur') 
    #     if self.vainqueur == 'programme':
    #         print('2 points programme')
                         
 


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())