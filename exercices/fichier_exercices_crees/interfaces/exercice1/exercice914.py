
import sys
from PyQt5 import   QtWidgets, uic


qtCreatorFile = "ui913.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Mon_horizontalSlider.valueChanged.connect(self.slider_value)   #<======
        
    def slider_value(self):                                                 #<======
        ma_valeur = self.Mon_horizontalSlider.value()                       #<======
        print(ma_valeur)                                                    #<======


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


