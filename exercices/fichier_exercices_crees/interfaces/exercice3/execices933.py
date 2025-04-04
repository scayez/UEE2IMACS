# 3- Connecter les boutons radio pour le choix des marques et créer la fonction marques. Cette fonction permettra d'affecter 'X' ou 'O' à self.marque en fonction du choix du joueur. 
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
        self.radioButton_o.clicked.connect(self.marques)#<===========
        self.radioButton_x.clicked.connect(self.marques)#<===========
               
    def marques(self):#<===========
        """3- Connecter les boutons radio pour le choix des marques et créer la fonction marques. Cette fonction permettra d'affecter
        'X' ou 'O' à self.marque en fonction du choix du joueur
        """
        if self.radioButton_o.isChecked():#<===========
            self.marque = 'O'#<===========
            print(self.marque)#<===========
            
        if self.radioButton_x.isChecked():#<===========
            self.marque = 'X'#<===========
            print(self.marque)#<===========
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


    sys.exit(app.exec_())

