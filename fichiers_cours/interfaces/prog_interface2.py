import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog


qtCreatorFile = "mon_interface2.ui" # Enter file here.
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
        fileName, _ = QFileDialog.getOpenFileName(self, "Ouvrir un fichier", "", "Tous les fichiers (*);;Fichiers texte (*.txt)", options=options)
        if fileName:
            print("Fichier sélectionné :", fileName)
            with open(fileName, "r") as file:
                contenu = file.read()
                print("Contenu du fichier :", contenu)




 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

