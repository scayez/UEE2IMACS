import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog   
from PyQt5.QtGui import QPixmap 
                    


qtCreatorFile = "ui925a.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.actionOuvrir.triggered.connect(self.ouvrir_fichiers)  
        self.pushButton_suivante.clicked.connect(self.suivante) 
        self.pushButton_precedente.clicked.connect(self.precedente) 
        
        self.image_a_afficher = 0 #Ininitialiser l'indice de l'image à afficher
        
        
    def ouvrir_fichiers(self):
        options = QFileDialog.Options()
        # Spécifie les filtres pour les fichiers image
        filters = "Images (*.png *.jpg *.jpeg)"    
        # Affiche la boîte de dialogue pour sélectionner un fichier
        # Sélectionnez les fichiers ATTENTION ici on utilise self pour avoir un attribut de classe et pouvoir l'appeler avec d'autres methodes
        self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", filters, options=options)  #<===========
 
        print(self.file_names)                     
        
        pixmap = QPixmap(self.file_names[self.image_a_afficher]) 
        self.label_image.setPixmap(pixmap)      
        self.label_image.setScaledContents(True)   
        #Définir la taille fixe du QLabel sur la taille de l'image
        self.label_image.setFixedSize(pixmap.size())  #<=========== 
        


    def suivante(self):     
                #Augmenter l'indice de l'image à afficher jusqu'au dernier indice, sinon repartir à zero
    
        if self.image_a_afficher < len(self.file_names)-1:
            self.image_a_afficher  += 1          

        else:                                         
            self.image_a_afficher = 0                

        
        pixmap = QPixmap(self.file_names[self.image_a_afficher]) 
        self.label_image.setPixmap(pixmap)      
        self.label_image.setScaledContents(True)    
        #Définir la taille fixe du QLabel sur la taille de l'image
        self.label_image.setFixedSize(pixmap.size())  #<=========== 
        
    def precedente(self):                                       
            
        #Diminuer l'indice l'image à afficher jusqu'au 0, sinon repartir au dernier indice
        if self.image_a_afficher >0:                           
            self.image_a_afficher  -= 1                        

        else:                                                      
            self.image_a_afficher = len(self.file_names)-1         

            
        pixmap = QPixmap(self.file_names[self.image_a_afficher])                                     
        # Affiche l'image dans le label
        self.label_image.setPixmap(pixmap)                             
        self.label_image.setScaledContents(True)                 #<=========== 


                 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

