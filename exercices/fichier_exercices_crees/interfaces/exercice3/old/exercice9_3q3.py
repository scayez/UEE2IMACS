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
        
        self.resultats = np.zeros((0, 2), dtype=int)
        self.marque = 'O'
        self.grille = np.zeros((3, 3), dtype=int)
        
        self.radioButton_o.clicked.connect(self.marques)#<===========
        self.radioButton_x.clicked.connect(self.marques)#<===========
        
    def marques(self):#<===========
        """Choix de la marque du joueur"""#<===========
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

