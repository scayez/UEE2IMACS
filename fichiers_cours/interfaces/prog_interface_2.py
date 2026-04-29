import sys
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma Fenêtre")
        self.setGeometry(100, 100, 400, 200)

        # Création d'un bouton
        self.button = QtWidgets.QPushButton("Quit", self)
        self.button.setGeometry(150, 80, 100, 30)

        # Connexion du clic du bouton à la fonction quit
        self.button.clicked.connect(self.quit) #<======

    # Définition de la fonction quit
    def quit(self): #<======
        print('Quit')
        self.close() #<======

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())





