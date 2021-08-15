from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexion

global indiceControl

def validarCampos():
    if ventana.txtNombre.text()==" " or ventana.txtCorreo.text()=="":
        alerta=QMessageBox()
        alerta.setText('¡ Debe llenar los campos')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True

def agregar():
    if validarCampos():
        return False
    print("Hola Soy la Accion de agregar")
    cedula=ventana.txtCedula.text()
    nombre=ventana.txtNombre.text()
    apellido=ventana.txtApellido.text()
    telefono=ventana.txtTelefono.text()
    correo=ventana.txtCorreo.text()
    print(nombre,apellido,telefono,correo)
    
    objContactos=conexion.contactos()
    contactos=objContactos.crearContacto((cedula, nombre, apellido, telefono, correo))
    consultar()
    
def eliminar():
    print("Hola Soy la Accion de eliminar") 
    cedula=ventana.txtCedula.text()
    objContactos=conexion.contactos()
    contactos=objContactos.borrarContacto(cedula)
    consultar()
 

def modificar():
    if validarCampos():
        return False
    print("Hola Soy la Acci{on de modificar")
    cedula=ventana.txtCedula.text()
    nombre=ventana.txtNombre.text()
    apellido=ventana.txtApellido.text()
    telefono=ventana.txtTelefono.text()
    correo=ventana.txtCorreo.text()
    print(nombre,apellido,telefono,correo)
    
    objContactos=conexion.contactos()
    contactos=objContactos.modificarContacto((nombre,apellido,telefono,correo,cedula))
    consultar()

def cancelar():
    print("Hola Soy la Acci{on de cancelar")  
    consultar()  
    
def consultar():
    ventana.tblContactos.setRowCount(0)
    indiceControl=0
    objContactos=conexion.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventana.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventana.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        indiceControl+=1
        
    ventana.txtCedula.setText("")
    ventana.txtNombre.setText("")
    ventana.txtApellido.setText("") 
    ventana.txtTelefono.setText("")
    ventana.txtCorreo.setText("")           
    
    ventana.btnAgregar.setEnabled(True)
    ventana.btnEliminar.setEnabled(False)
    ventana.btnModificar.setEnabled(False)
    ventana.btnCancelar.setEnabled(False)

def seleccionar():
    cedula=ventana.tblContactos.selectedIndexes()[0].data()
    nombre=ventana.tblContactos.selectedIndexes()[1].data()
    apellido=ventana.tblContactos.selectedIndexes()[2].data()
    telefono=ventana.tblContactos.selectedIndexes()[3].data()
    correo=ventana.tblContactos.selectedIndexes()[4].data()
    print(cedula, nombre, apellido, telefono, correo)
    ventana.txtCedula.setText(cedula)
    ventana.txtNombre.setText(nombre)
    ventana.txtApellido.setText(apellido)
    ventana.txtTelefono.setText(telefono)
    ventana.txtCorreo.setText(correo)
    
    ventana.btnAgregar.setEnabled(False)
    ventana.btnEliminar.setEnabled(True)
    ventana.btnModificar.setEnabled(True)
    ventana.btnCancelar.setEnabled(True)

    indiceControl=0
    objContactos=conexion.contactos()
    contactos=objContactos.leerContactos()
    for contacto in contactos:
        ventana.tblContactos.setRowCount(indiceControl+1)
        ventana.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventana.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventana.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventana.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventana.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        indiceControl+=1
    

aplicacion= QtWidgets.QApplication([])
ventana= uic.loadUi("ventana.ui")
ventana.show()
consultar()

ventana.tblContactos.setHorizontalHeaderLabels(['Cedula','Nombre','Apellidos','Telefono','Correo'])
ventana.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventana.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventana.tblContactos.cellClicked.connect(seleccionar)

ventana.btnAgregar.clicked.connect(agregar)
ventana.btnEliminar.clicked.connect(eliminar)
ventana.btnModificar.clicked.connect(modificar)
ventana.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())