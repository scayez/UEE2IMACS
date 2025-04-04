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
import pyqtgraph as pg


qtCreatorFile = "exercice9_3.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Jeu de Morpion")
        
        
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
        # initialiser le decompte des points
        self.score = np.zeros((1,2))
        
        
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
           
            if self.marque == "X" :
                self.grille[ligne][colonne] = 0  # jouer la marque que n'a pas choisi le joueur

            else:
                self.grille[ligne][colonne] = 1 
               
            # Mettez à jour l'affichage des X et O sur les boutons'
            self.actualiser_bouton()
            
            
        
    def actualiser_bouton(self):
        
        indices_zero = np.where(self.grille == 0)
        indices_un = np.where(self.grille == 1)
    
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
                   
                     self.vainqueur = 'joueur'
                     self.compter_points()
            if np.all(np.diag(self.grille) == 0) or np.all(np.diag(np.fliplr(self.grille)) == 0):
                     self.vainqueur = 'joueur'
                     self.compter_points()

        for i in range(3):
            if np.all(self.grille[:, i] == 1) or np.all(self.grille[i, :] == 1):
                self.vainqueur = 'programme'
                self.compter_points()
               
        if np.all(np.diag(self.grille) == 1) or np.all(np.diag(np.fliplr(self.grille)) ==1):
                self.vainqueur = 'programme'
                self.compter_points()
                      
                
        
        if self.marque == 'X':
             for i in range(3):
                 if np.all(self.grille[:, i] == 1) or np.all(self.grille[i, :] == 1): 
                     self.vainqueur = 'joueur'
                     self.compter_points()
                     

             if np.all(np.diag(self.grille) == 1) or np.all(np.diag(np.fliplr(self.grille)) ==1):
                 self.vainqueur = 'joueur'
                 self.compter_points()

                
     
             for i in range(3):
                 if np.all(self.grille[:, i] == 0) or np.all(self.grille[i, :] == 0):
                     self.vainqueur = 'programme'
                     self.compter_points()
             if np.all(np.diag(self.grille) == 0) or np.all(np.diag(np.fliplr(self.grille)) == 0):
                     self.vainqueur = 'programme'
                     self.compter_points()
             
                
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

    def compter_points(self):
        points = self.spinBox_niveau.value()
        print(points)
        
        if self.vainqueur == 'joueur':
            
        
            self.afficher_message('Joueur gagne', '1 point joueur')
            self.score = np.append(self.score , [[1, 0]], axis=0)
            # print(self.score) 
            
        if self.vainqueur == 'programme':
           
            self.afficher_message('Programme gagne', f'{points} point programme')
            self.score = np.append(self.score , [[0, points]], axis=0)
  
        self.plot()
            
            
    def plot(self):
        
        # Récupérer les indices des colonnes
       indices = list(range(self.score.shape[0]))

       # Initialiser les scores cumulatifs pour chaque joueur
       score_joueur_cumulatif = 0
       score_programme_cumulatif = 0

       # Listes pour stocker les scores cumulatifs
       scores_joueur = []
       scores_programme = []

       # Itérer sur les parties
       for partie_numero in range(self.score.shape[0]):
           # Mettre à jour les scores cumulatifs
           score_joueur_cumulatif += self.score[partie_numero, 0]
           score_programme_cumulatif += self.score[partie_numero, 1]

           # Ajouter les scores cumulatifs aux listes
           scores_joueur.append(score_joueur_cumulatif)
           scores_programme.append(score_programme_cumulatif)
           


        # Tracer les scores cumulatifs pour chaque joueur
       self.plot_widget.plot(indices, scores_joueur, pen=pg.mkPen(color='r', width=2), symbol='o', name='Score Joueur')
       self.plot_widget.plot(indices, scores_programme, pen=pg.mkPen(color='b', width=2), symbol='o', name='Score Programme')
       
       self.label_score_joueur.setText(str(score_joueur_cumulatif))
       self.label_score_programme.setText(str(score_programme_cumulatif))
     
        
             

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())