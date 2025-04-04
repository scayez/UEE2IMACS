# 2- Initialiser les variables suivantes:
# self.resultats sera un tableau numpy rempli de zeros de dimension 0 lignes et 2 colonnes et de type entier. Il servira a stocker les scores du joueur et du programme.
# self.marque sera un caractére qui peut être 'O' ou 'X' , nous choisirons 'O' qui sera la marque par défaut pour le joueur
# self.grille sera un tableau numpy rempli de zeros de dimension 3 lignes et 3 colonnes et de type entier. Il représentera la grille de jeu.

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
        self.resultats = np.zeros((0, 2), dtype=int)#<===========
        self.marque = 'O'#<===========
        self.grille = np.full((3, 3), 2, dtype=int)#<=========== 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

