#11- Ajouter l'option de niveau: en cas de victoire, le programme marque le nombre de points de la spinbox. Les modifications sont dans compter points.
import sys
from PyQt5 import   QtWidgets, uic
import numpy as np
import random
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph as pg#<===========

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
        #Connecter le bouton rejouer
        self.pushButton_rejouer.clicked.connect(self.initialiser)
        
        #vider la grille
        self.initialiser()
        # initialiser le decompte des points
        self.score = np.zeros((1,2))
             
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
            
        # Jouer un coup aléatoire pour le programme  
        self.jouer_coup_aleatoire()
        print('---------------------------')
        self.actualiser_bouton()
        #Appeler la fonction pour vérifier le gagnant
        print(self.grille)
        self.verif_gagnant()
        
    def jouer_coup_aleatoire(self):
        """
         5- passer la valeur correspondant à la position dans le tableau numpy à 0 si le joueur a choisi X ou à 1 si le joueur a choisi 0.
        """
        cases_disponibles = [(i, j) for i in range(3) for j in range(3) if self.grille[i][j] == 2]
        if cases_disponibles:
            ligne, colonne = random.choice(cases_disponibles)       
            if self.marque == "X" :
                self.grille[ligne][colonne] = 0  # jouer la marque que n'a pas choisi le joueur     
            else:
                self.grille[ligne][colonne] = 1              
            # Mettez à jour l'interface graphique
            self.actualiser_bouton()         
        
    def actualiser_bouton(self):
        """
         6- Actualiser le texte des boutons de manière à faire apparaitre le X ou le O sur le bouton joué
        """
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
        """
        7- verifier si le joueur ou le programme a fait une ligne une colonne ou une diagonale
        """
        # Vérification des lignes et colonnes
        if self.marque == 'O':
            for i in range(3):
                #Vérification des lignes et colonnes
                if np.all(self.grille[:, i] == 0) or np.all(self.grille[i, :] == 0):
                     self.vainqueur = 'joueur' 
                     self.compter_points() 
            #Vérification des diagonales
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
           """
           8- Vider la grille et effacer le texte des boutons pour une nouvelle partie
           """    
           #initialisations des variables
           self.resultats = np.zeros((0, 2), dtype=int) 
           self.marque = 'O' 
           self.radioButton_o.setChecked(True)
           self.grille = np.full((3, 3), 2, dtype=int)
           
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

    def compter_points(self): 
        """
        9- Remplir un tableau numpy avec 2 colonne (1 pour le joueur, 1 pour le programme) à chaque 
        tour on ajoutera une ligne avec 1 pour le gagnant 0 pour le perdant.
        11- Ajouter l'option de niveau: en cas de victoire, le programme marque le nombre de points de la spinbox. Les modifications sont dans compter points. 
        """
        points = self.spinBox_niveau.value()#<===========
        print(points)#<===========
        if self.vainqueur == 'joueur':

            self.afficher_message('Joueur gagne', '1 point joueur')
            self.score = np.append(self.score , [[1, 0]], axis=0)
            print(self.score) 
            
        if self.vainqueur == 'programme':
           
            self.afficher_message('Programme gagne', str(points)+' point(s) programme')#<===========
            self.score = np.append(self.score , [[0, points]], axis=0)#<===========#on remplace 1 par points
            print(self.score)      
        self.plot()  
    def afficher_message(self, titre, message):
        """
        9- Ouvrir une messageBox indiquant le vainqueur et initialiser la grille et les boutons
        """
    
        msg_box = QMessageBox() 
        msg_box.setWindowTitle(titre) 
        msg_box.setText(message) 
        msg_box.exec_() 
        #la partie est finie, on initialise
        self.initialiser()  
        
           
    def plot(self):
      """
      10-calcul score_joueur_cumulatif et score_programme_cumulatif, les sommes des scores de chacun au cours des parties.
      On tracera les evolutions des scores du joueur et du programmeau fil des parties.        
      """
       
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
