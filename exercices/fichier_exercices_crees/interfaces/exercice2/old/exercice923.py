#4- Modifier la fonction ouvrir_fichiers pour utiliser QFileDialog.getOpenFileNames qui permettra la selection de plusieurs fichiers et renverra une liste de chemins. 
#faire un print des chemins des fichiers selectionnée. (Dans un premier temps on mettra la conversion en pixmap et l'affichage dans le label en commentaire pour éviter les erreurs à l'execution.
import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog   
from PyQt5.QtGui import QPixmap                        


qtCreatorFile = "ui921.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir_fichiers)   
        
        
    def ouvrir_fichiers(self):
        #options = QFileDialog.Options()
        # Spécifie les filtres pour les fichiers image
        #filters = "Images (*.png *.jpg *.jpeg)"    
        # Affiche la boîte de dialogue pour sélectionner un fichier
        # Sélectionnez les fichiers ATTENTION ici on utilise self pour avoir un attribut de classe et pouvoir l'appeler avec d'autres methodes
        #self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", filters, options=options)  #<===========
        self.fileNames, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "",  "Images (*.png *.jpg *.jpeg)") 
        print(self.file_names)                     
        
        pixmap = QPixmap(self.fileNames)       #<===========                            
        #Affiche l'image dans le label
        self.label_image.setPixmap(pixmap)   #<===========                       

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

