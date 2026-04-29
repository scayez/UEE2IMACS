# Importation du module sys pour accéder aux arguments de la ligne de commande
import sys
# Importation de la classe QtWidgets de PyQt5
from PyQt5 import QtWidgets  
# Définition d'une nouvelle classe MyWindow qui hérite de QMainWindow
class MyWindow(QtWidgets.QMainWindow):  
    def __init__(self):  # Définition du constructeur de la classe
        super().__init__()  # Appel du constructeur de la classe parent QMainWindow
        self.setWindowTitle("Ma Fenêtre")  # Définition du titre de la fenêtre
        self.setGeometry(100, 100, 400, 200)  # Définition de la position et de la taille de la fenêtre

if __name__ == "__main__":  # Point d'entrée du programme
    app = QtWidgets.QApplication(sys.argv)  # Création d'une instance de QApplication avec les arguments du programme
    window = MyWindow()  # Création d'une instance de la classe MyWindow
    window.show()  # Affichage de la fenêtre
    sys.exit(app.exec_())  # Boucle principale de l'application PyQt, qui attend que l'application se termine avant de quitter

