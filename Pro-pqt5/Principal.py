import sys
from PyQt5 import uic, QtWidgets
from Principal import Ui_MainWindow

qtCreatorFile = "menu.ui" 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
           
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.BtnTablaPersonas.clicked.connect(self.abrir1)
    
    def abrir1 (self):
        self.ventana=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()  
 
if __name__ == "_main_":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()