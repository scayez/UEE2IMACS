import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap                         #<===========

qtCreatorFile = "exercice9_2.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir)        
        
 
        
    def ouvrir(self):
        options = QFileDialog.Options()
    
        # Spécifie les filtres pour les fichiers image
        filters = "Images (*.png *.jpg *.jpeg);;Tous les fichiers (*)"
    
        # Affiche la boîte de dialogue pour sélectionner un fichier
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", filters, options=options)
        
        # Vérifie si un fichier a été sélectionné
        if fileName:
            # Traitez le fichier sélectionné (fileName)
            print(f"Fichier sélectionné : {fileName}")
            # Crée un objet QPixmap à partir du fichier image
            
            pixmap = QPixmap(fileName)                                    #<===========
            # Affiche l'image dans le label
            self.label_image.setPixmap(pixmap)                           #<===========
            self.label_image.setScaledContents(True)  # Pour maintenir le ratio d'aspect#<===========



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
