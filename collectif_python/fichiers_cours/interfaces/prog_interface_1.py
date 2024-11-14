import sys
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ma Fenêtre")
        self.setGeometry(100, 100, 400, 200)

        # Création d'un bouton
        self.button = QtWidgets.QPushButton("Cliquez moi !", self) #<======
        self.button.setGeometry(150, 80, 100, 30) #<======

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())



