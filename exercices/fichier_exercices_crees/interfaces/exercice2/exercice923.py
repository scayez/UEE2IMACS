import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap #<-------------


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
       file_name, _ = QFileDialog.getOpenFileName(self, "Ouvrir un ou plusieurs fichiers", "", "Images (*.png *.jpg *.jpeg)") #<-------------
       if file_name:
           print("Fichiers sélectionnés :", type(file_name))
           # Affichage de la première image de la liste
           pixmap = QPixmap(file_name)#<-------------
           self.label_image.setPixmap(pixmap)#<-------------
           self.label_image.setScaledContents(True)#<-------------        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
