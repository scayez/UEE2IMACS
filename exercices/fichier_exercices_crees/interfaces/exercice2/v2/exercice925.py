import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap

# Chargement de l'interface (ici le fichier ui925.ui est utilisé comme exemple)
qtCreatorFile = "ui925a.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir_fichiers)
        self.pushButton_suivante.clicked.connect(self.suivante)#<-------------
        self.pushButton_precedente.clicked.connect(self.precedente)#<-------------
        
        self.file_names = []  # Liste des chemins des images sélectionnées #<-------------
        self.image_a_afficher = 0  # Indice de l'image actuellement affichée #<-------------
        
    def ouvrir_fichiers(self):
        # Utilisation de getOpenFileNames pour sélectionner plusieurs images
        self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", "Images (*.png *.jpg *.jpeg)")
        if self.file_names:
            print("Fichiers sélectionnés :", self.file_names)
            # Affichage de la première image de la liste
            pixmap = QPixmap(self.file_names[self.image_a_afficher])
            self.label_image.setPixmap(pixmap)
            self.label_image.setScaledContents(True)

    def suivante(self): #<-------------
        # Incrémente l'indice et revient à 0 si on dépasse le dernier indice #<-------------
        if self.image_a_afficher < len(self.file_names) - 1: #<-------------
            self.image_a_afficher += 1#<-------------
        else:  #<-------------
            self.image_a_afficher = 0 #<-------------
            
        pixmap = QPixmap(self.file_names[self.image_a_afficher])#<-------------
        self.label_image.setPixmap(pixmap)#<-------------
        self.label_image.setScaledContents(True)#<-------------

    def precedente(self):#<-------------
        # Décrémente l'indice et passe au dernier indice si on est au début#<-------------
        if self.image_a_afficher > 0:#<-------------
            self.image_a_afficher -= 1#<-------------
        else:#<-------------
            self.image_a_afficher = len(self.file_names) - 1#<-------------
            
        pixmap = QPixmap(self.file_names[self.image_a_afficher])#<-------------
        self.label_image.setPixmap(pixmap)#<-------------
        self.label_image.setScaledContents(True)#<-------------

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
