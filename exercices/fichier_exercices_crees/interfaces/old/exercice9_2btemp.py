from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


import sys
from PyQt5 import   QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap  

qtCreatorFile = "exercice9_2.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        # Créez une étiquette pour afficher les images
        self.label_image = QLabel(self)

        # Créez un bouton pour afficher l'image suivante
        self.button_suivante = QPushButton("Image suivante", self)
        self.button_suivante.clicked.connect(self.suivante)

        # Initialisez l'indice de l'image actuellement affichée
        self.current_index = 0

        # Ajoutez la disposition (layout) pour organiser les widgets
        layout = QVBoxLayout()
        layout.addWidget(self.label_image)
        layout.addWidget(self.button_suivante)

        # Créez un widget principal et définissez la disposition
        main_widget = QWidget(self)
        main_widget.setLayout(layout)

        # Définissez le widget principal comme widget central de la fenêtre principale
        self.setCentralWidget(main_widget)

    def ouvrir(self):
        # Options de la boîte de dialogue pour la sélection de fichiers
        options = QFileDialog.Options()

        # Filtres pour les fichiers image
        filters = "Images (*.png *.jpg *.jpeg *.tif *.bmp);;Tous les fichiers (*)"
    
        # Sélectionnez les fichiers à l'aide de la boîte de dialogue
        self.file_names, _ = QFileDialog.getOpenFileNames(self, "Ouvrir un ou plusieurs fichiers", "", filters, options=options)

        if self.file_names:
            # Chargez la première image et affichez-la
            self.afficher_image()

    def suivante(self):
        # Affichez l'image suivante lorsqu'on appuie sur le bouton "Image suivante"
        if self.file_names and self.current_index < len(self.file_names) - 1:
            self.current_index += 1
            self.afficher_image()

    def afficher_image(self):
        # Chargez l'image en utilisant l'indice actuel
        pixmap = QPixmap(self.file_names[self.current_index])
        
        # Redimensionnez l'image pour forcer la hauteur à 300 pixels
        pixmap_scaled = pixmap.scaledToHeight(300)

        # Affichez l'image dans l'étiquette
        self.label_image.setPixmap(pixmap_scaled)

        # Permettez le redimensionnement de l'image pour s'adapter à l'étiquette
        self.label_image.setScaledContents(True)

if __name__ == '__main__':
    # Créez une application PyQt
    app = QApplication([])

    # Créez une instance de la classe MaFenetre
    fenetre = MaFenetre()

    # Appelez la fonction pour ouvrir les fichiers
    fenetre.ouvrir()

    # Affichez la fenêtre
    fenetre.show()

    # Exécutez l'application
    app.exec_()


