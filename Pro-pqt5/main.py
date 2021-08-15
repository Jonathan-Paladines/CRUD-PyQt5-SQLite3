import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import uic
import os


class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("menu.ui", self)
        self.BtnTablaPersonas.clicked.connect(self.conectar1)
        #self.ventana = Ventana()
        self.BtnTablaProductos.clicked.connect(self.conectar2)
        #self.ventanavista = VentanaVista()
        self.BtnGenerarArchivo.clicked.connect(self.conectar3)
        self.BtnSalir.clicked.connect(self.conectar4)
        
    '''def showEvent (self, event):
        self.lbl_bienvenida.setText("Bienvenido a la aplicación")'''
        
    def conectar1(self):
        os.system('python crud.py')  #llamamos al archivo que eduta la tabla Contactos
        #self.ventana.exec_()
        
    def conectar2(self):
        os.system('python crudproducto.py')  #llamamos al archivo que edita la tabla producto
        #self.ventanavista.exec_()

    def conectar3(self):
        os.system('python lreporte.py') #llamamos al archivo reporte
        #self.ventanavista.exec_()   
    
    def conectar4(self):
        sys.exit()     

class Ventana(QDialog):
    def __init__(self):
        #os.system('python crudproducto.py')
        QDialog.__init__(self)
        uic.loadUi("ventana.ui", self)

class VentanaVista(QDialog):
    def __init__(self):
        #os.system('python crud.py')
        QDialog.__init__(self)
        uic.loadUi("ventanavista.ui", self)
        
app=QApplication(sys.argv)
principal = Principal()
principal.show()
app.exec_()