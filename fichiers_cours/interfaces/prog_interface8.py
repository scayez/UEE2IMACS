import sys
from PyQt5 import  QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import pyqtgraph as pg
import numpy as np


qtCreatorFile = "mon_interface8.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.pushButton_quit.clicked.connect(self.quit)
        self.actionOpen.triggered.connect(self.ouvrir)
        
        # Connexion du signal activated de la combobox à la fonction calculs
        self.Ma_comboBox.activated.connect(self.calculs)
        
        #Modifier le titre de la fenêtre:
        self.setWindowTitle("Mon Premier Programme Avec Interface")
                
        # Ajouter une icône à la fenêtre
        # self.setWindowIcon(QtGui.QIcon('poisson.png'))
        icon = QtGui.QIcon("mon_icone.png")  # Spécifiez le chemin vers votre icône
        self.setWindowIcon(icon)

    def quit(self):   
         
        self.close()
        
    def ouvrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Fichiers texte (*.txt)", options=options)
        if fileName:
            print("Fichier sélectionné :", fileName)
            df = pd.read_csv(fileName, sep='\t', header=0, usecols=[0, 1])
            self.data = df.values # on ajoute self pour pouvoir utiliser la variable dans une autre fonction de la classe
            print("Données extraites :", self.data.shape)
            self.plot()  # on appelle la fonction qui trace le graph
       
    def plot(self):
         
        self.plot_widget.plot(self.data, pen=pg.mkPen(color='r', width=2))  # Tracer les données (x, y)

    def calculs(self):
    # Récupérer la sélection de la combobox
        selected_item = self.Ma_comboBox.currentText()

        # Effectuer les calculs en fonction de l'élément sélectionné
        if selected_item == "Minimum":
            result = np.min(self.data[:, 1])
        elif selected_item == "Maximum":
            result = np.max(self.data[:, 1])
        elif selected_item == "Moyenne":
            result = np.mean(self.data[:, 1])
        elif selected_item == "Ecart Type":
            result = np.std(self.data[:, 1])
        else:
            result = None

        # Afficher le résultat dans le label
        if result is not None:
            texte_affichage = selected_item+': '+": {:.3f}".format(result)
            print(texte_affichage)
            self.Ma_label.setText(texte_affichage)
        else:
            self.Ma_label.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())