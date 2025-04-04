import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap 


# Chargement de l'interface créée avec Qt Designer
qtCreatorFile = "ui921.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Le menu "Ouvrir" sera connecté à la fonction ouvrir_fichiers dans l'étape suivante
        self.actionOuvrir.triggered.connect(self.ouvrir_fichiers)


    def ouvrir_fichiers(self):
            # Utilisation de getOpenFileNames pour sélectionner plusieurs fichiers
            # Avec un s!
            self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", "Images (*.png *.jpg *.jpeg)") #<-------------
            if self.file_names:#<-------------
                print("Fichiers sélectionnés :", self.file_names)#<-------------
                # Pour le moment, on commente l'affichage pour éviter les erreurs
                # pixmap = QPixmap(self.file_names[0])
                # self.label_image.setPixmap(pixmap)
                # self.label_image.setScaledContents(True)        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


