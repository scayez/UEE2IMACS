import sys
from PyQt5 import   QtWidgets, uic


try:
    qtCreatorFile = "fichiers_cours/interfaces/mon_interface0.ui" # Essayer d'ouvrir ce fichier.
    with open(qtCreatorFile):
        pass  # Si le fichier existe, ne rien faire.
except FileNotFoundError:
    qtCreatorFile = "mon_interface0.ui"  # Si le fichier n'existe pas, utiliser un chemin de secours.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())







