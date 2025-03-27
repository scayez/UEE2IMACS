import sys
from PyQt5 import  QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import pandas as pd
import pyqtgraph as pg


try:
    qtCreatorFile = "fichiers_cours/interfaces/mon_interface3.ui" # Essayer d'ouvrir ce fichier.
    with open(qtCreatorFile):
        pass  # Si le fichier existe, ne rien faire.
except FileNotFoundError:
    qtCreatorFile = "mon_interface3.ui"  # Si le fichier n'existe pas, utiliser un chemin de secours.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        self.pushButton_quit.clicked.connect(self.quit)
        self.actionOpen.triggered.connect(self.ouvrir)
        
        

    def quit(self):   
        self.close()
        
    def ouvrir(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Fichiers texte (*.txt)", options=options)
        if fileName:
            print("Fichier sélectionné :", fileName)
            df = pd.read_csv(fileName, sep='\t', header=0, usecols=[0, 1])
            self.data = df.values # on ajoute self pour pouvoir utiliser la variable dans une autre fonction de la classe
            # print("Données extraites :", self.data)
            self.plot()  # on appelle la fonction qui trace le graph

    def plot(self):
        self.plot_widget.plot(self.data, pen=pg.mkPen(color='r', width=2))  # Tracer les données (x, y)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())









