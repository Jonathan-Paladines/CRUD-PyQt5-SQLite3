from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import os
from io import open
import conexionreporte

global indiceControl

def accion_de_mi_boton():
    os.system('python conexionreporte2.py')
    print("Mi botón ha sido presionado")

    
def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl=0
    objContactos=conexionreporte.reporte()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventana.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventana.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        ventana.tblContactos.setItem(indiceControl,5, QTableWidgetItem(str(contacto[5])))
        ventana.tblContactos.setItem(indiceControl,6, QTableWidgetItem(str(contacto[6])))
        ventana.tblContactos.setItem(indiceControl,7, QTableWidgetItem(str(contacto[7])))
        ventana.tblContactos.setItem(indiceControl,8, QTableWidgetItem(str(contacto[8])))        
        indiceControl+=1
         

def seleccionar():
    cedula=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    apellido=ventana.tblContactos.selectedIndexes()[2].data()
    telefono=ventana.tblContactos.selectedIndexes()[3].data()
    correo=ventana.tblContactos.selectedIndexes()[4].data()
    codigo=ventana.tblContactos.selectedIndexes()[5].data()
    producto=ventana.tblContactos.selectedIndexes()[6].data()    
    cantidad=ventana.tblContactos.selectedIndexes()[7].data()
    valor=ventana.tblContactos.selectedIndexes()[8].data()
    
    print(cedula, nombre, apellido, telefono, correo, codigo, producto, cantidad, valor)


    indiceControl=0
    objContactos=conexionreporte.reporte()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventana.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventana.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        ventana.tblContactos.setItem(indiceControl,5, QTableWidgetItem(str(contacto[5])))
        ventana.tblContactos.setItem(indiceControl,6, QTableWidgetItem(str(contacto[6])))
        ventana.tblContactos.setItem(indiceControl,7, QTableWidgetItem(str(contacto[7])))
        ventana.tblContactos.setItem(indiceControl,8, QTableWidgetItem(str(contacto[8])))        
        indiceControl+=1
    

aplicacion= QtWidgets.QApplication([])
ventana= uic.loadUi("vista.ui")
ventana.show()
consultar()

ventana.tblContactos.setHorizontalHeaderLabels(['Cedula','Nombre','Apellidos','Telefono','Correo','Codigo','Producto','Cantidad','Valor'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect(seleccionar)

ventana.BtnExport.clicked.connect(accion_de_mi_boton)

sys.exit(aplicacion.exec())
