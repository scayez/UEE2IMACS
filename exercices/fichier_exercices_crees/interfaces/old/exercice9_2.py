# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 16:12:47 2024

@author: cayez
"""

import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog , QMessageBox   #<===========
from PyQt5.QtGui import QPixmap  , QImage                       #<===========
import numpy as np
import matplotlib.pyplot as plt

qtCreatorFile = "exercice9_2.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Mon_horizontalSlider.valueChanged.connect(self.slider_value)
        self.actionOuvrir.triggered.connect(self.ouvrir)  
        self.pushButton_gris.clicked.connect(self.convertir_gris)    #<===========  
        
    def slider_value(self):                                                 
        ma_valeur = self.Mon_horizontalSlider.value()                       
        print(ma_valeur) 
        self.Mon_label.setText(str(ma_valeur))  
        
    def ouvrir(self):
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog  # Utilise le dialogue de fichier Qt plutôt que celui du système d'exploitation
    
        # Spécifie les filtres pour les fichiers image
        filters = "Images (*.png *.jpg *.jpeg);;Tous les fichiers (*)"
    
        # Affiche la boîte de dialogue pour sélectionner un fichier
        self.fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", filters, options=options)
        
        # Vérifie si un fichier a été sélectionné
        if self.fileName:
            try: 
                # Traitez le fichier sélectionné (fileName)
                print(f"Fichier sélectionné : {self.fileName}")
                # Crée un objet QPixmap à partir du fichier image
                pixmap = QPixmap(self.fileName)                                    
                # Affiche l'image dans le label
                self.label_image.setPixmap(pixmap)                           
                self.label_image.setScaledContents(True)  # Pour maintenir le ratio d'aspect#
            except:
                #Créez une boîte de dialogue de type warning
                warning_box = QMessageBox()
                warning_box.setIcon(QMessageBox.Warning)
                warning_box.setWindowTitle("Avertissement")
                warning_box.setText("Le format du Fichier n'est pas compatible.")  # 
                warning_box.setStandardButtons(QMessageBox.Ok)
                
    def convertir_gris(self):
        
        image_array = plt.imread(self.fileName)
        print(image_array.shape)
        red_channel = image_array[:, :, 0]
        green_channel = image_array[:, :, 1]
        blue_channel = image_array[:, :, 2]
        image_gray = (red_channel/3 + green_channel/3 + blue_channel/3) 
        
        # Sélectionnez les trois premiers canaux (RGB)
        # rgb_data = image_array[:, :, :3]
        
        print(image_gray.shape)
        # # Calculez la moyenne des trois premiers canaux
        # average_rgb = np.mean(rgb_data, axis=(0, 1))
        # qImg = QPixmap(QImage(average_rgb.data, average_rgb.shape[0], average_rgb.shape[1], QImage.Format_RGB888))
        # self.label_image.setPixmap(average_rgb)
                

                                               


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

