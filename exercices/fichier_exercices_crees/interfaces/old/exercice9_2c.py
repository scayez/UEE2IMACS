import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap                         

qtCreatorFile = "exercice9_2.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir) 
        self.pushButton_suivante.clicked.connect(self.suivante)
        self.pushButton_precedente.clicked.connect(self.precedente)
        
        self.current_index = 0 #Ininitialiser l'indice de l'image à afficher

        
    def ouvrir(self):
        options = QFileDialog.Options()
        # Spécifiez les filtres pour les fichiers image
        filters = "Images (*.png *.jpg *.jpeg *.tif *.bmp);;Tous les fichiers (*)"
    
        # Sélectionnez les fichiers ATTENTION ici on utilise self pour avoir un attribut de classe et pouvoir l'appeler avec d'autres methodes
        self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", filters, options=options)

        if self.file_names:
            pixmap = QPixmap(self.file_names[self.current_index])                                    
            # Affiche l'image dans le label
            self.label_image.setPixmap(pixmap)                        
            self.label_image.setScaledContents(True) 
            
            
    def suivante(self):
            #Augmenter l'indice de l'image à afficher jusqu'au dernier indice, sinon repartir à zero

            if self.current_index < len(self.file_names)-1:
                self.current_index  += 1

            else: 
                self.current_index = 0

            
            pixmap = QPixmap(self.file_names[self.current_index])                                    
            # Affiche l'image dans le label
            self.label_image.setPixmap(pixmap)                        
            self.label_image.setScaledContents(True)
            
    def precedente(self):
        
            #Diminuer l'indice l'image à afficher jusqu'au 0, sinon repartir au dernier indice
            if self.current_index >0:
                self.current_index  -= 1

            else: 
                self.current_index = len(self.file_names)-1

                
            pixmap = QPixmap(self.file_names[self.current_index])                                    
            # Affiche l'image dans le label
            self.label_image.setPixmap(pixmap)                        
            self.label_image.setScaledContents(True)
          
                  



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
