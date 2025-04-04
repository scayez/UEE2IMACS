# 2- Connecter le menu ouvrir à une fonction ouvrir_fichiers. On pourra limiter le type de fichier aux principaux types de fichiers image (png, jpg, jpeg...)  
# Faire un print du nim de fichier crée.
import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog   #<===========


qtCreatorFile = "ui921.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir_fichiers)    #<===========
        
        
    def ouvrir_fichiers(self):
 
        #Affiche la boîte de dialogue pour sélectionner un fichier #<===========
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "",  "Images (*.png *.jpg *.jpeg)")  #<===========
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())



