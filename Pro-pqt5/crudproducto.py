from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import conexionproducto

global indiceControl

def validarCampos():
    if ventanap.txtProducto.text()==" " or ventanap.txtValor.text()=="":
        alerta=QMessageBox()
        alerta.setText('¡ Debe llenar los campos')
        alerta.setIcon(QMessageBox.Information)
        alerta.exec()
        return True

def agregar():
    if validarCampos():
        return False
    print("Hola Soy la Accion de agregar")
    codigo=ventanap.txtCodigo.text()
    producto=ventanap.txtProducto.text()
    cantidad=ventanap.txtCantidad.text()
    valor=ventanap.txtValor.text()
    cedula=ventanap.txtCed.text()
    print(codigo,producto,cantidad,valor,cedula)
    
    objProducto=conexionproducto.productos()
    producto12=objProducto.crearContacto((codigo,producto,cantidad,valor,cedula))
    consultar()
    
def eliminar():
    print("Hola Soy la Accion de eliminar") 
    codigo=ventanap.txtCed.text()
    objProducto=conexionproducto.productos()
    producto12=objProducto.borrarContacto(codigo)
    consultar()

 

def modificar():
    if validarCampos():
        return False
    print("Hola Soy la Acci{on de modificar")
    codigo=ventanap.txtCodigo.text()
    producto=ventanap.txtProducto.text()
    cantidad=ventanap.txtCantidad.text()
    valor=ventanap.txtValor.text()
    cedula=ventanap.txtCed.text()
    print(codigo,producto,cantidad,valor,cedula)
    
    objProducto=conexionproducto.productos()
    producto12=objProducto.modificarContacto((producto,cantidad,valor,cedula,codigo))
    consultar()

def cancelar():
    print("Hola Soy la Acci{on de cancelar")  
    consultar()  
    
def consultar():
    ventanap.tblContactos.setRowCount(0)
    indiceControl=0
    objContactos=conexionproducto.productos()
    produc=objContactos.leerContactos()
    
    # ventanap.tblContactos.selectedIndexes()[0].data()
    # ventanap.tblContactos.selectedIndexes()[1].data()
    # ventanap.tblContactos.selectedIndexes()[2].data()
    # ventanap.tblContactos.selectedIndexes()[3].data()
    # ventanap.tblContactos.selectedIndexes()[4].data()
    
    print(produc)
    
    for contacto in produc:
        ventanap.tblContactos.setRowCount(indiceControl+1)
        ventanap.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventanap.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventanap.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventanap.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventanap.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        indiceControl+=1
        
    ventanap.txtCodigo.setText("")
    ventanap.txtProducto.setText("")
    ventanap.txtCantidad.setText("") 
    ventanap.txtValor.setText("")
    ventanap.txtCed.setText("")           
    
    ventanap.btnAgregar.setEnabled(True)
    ventanap.btnEliminar.setEnabled(False)
    ventanap.btnModificar.setEnabled(False)
    ventanap.btnCancelar.setEnabled(False)

def seleccionar():
    codigo=ventanap.tblContactos.selectedIndexes()[0].data()
    producto=ventanap.tblContactos.selectedIndexes()[1].data()
    cantidad=ventanap.tblContactos.selectedIndexes()[2].data()
    valor=ventanap.tblContactos.selectedIndexes()[3].data()
    cedula=ventanap.tblContactos.selectedIndexes()[4].data()
    print(codigo,producto,cantidad,valor,cedula)
    ventanap.txtCodigo.setText(codigo)
    ventanap.txtProducto.setText(producto)
    ventanap.txtCantidad.setText(cantidad)
    ventanap.txtValor.setText(valor)
    ventanap.txtCed.setText(cedula)
    
    ventanap.btnAgregar.setEnabled(False)
    ventanap.btnEliminar.setEnabled(True)
    ventanap.btnModificar.setEnabled(True)
    ventanap.btnCancelar.setEnabled(True)

    indiceControl=0
    objContactos=conexionproducto.productos()
    produc=objContactos.leerContactos()
    for contacto in produc:
        ventanap.tblContactos.setRowCount(indiceControl+1)
        ventanap.tblContactos.setItem(indiceControl,0, QTableWidgetItem(str(contacto[0])))
        ventanap.tblContactos.setItem(indiceControl,1, QTableWidgetItem(str(contacto[1])))
        ventanap.tblContactos.setItem(indiceControl,2, QTableWidgetItem(str(contacto[2])))
        ventanap.tblContactos.setItem(indiceControl,3, QTableWidgetItem(str(contacto[3])))
        ventanap.tblContactos.setItem(indiceControl,4, QTableWidgetItem(str(contacto[4])))
        indiceControl+=1
    

aplicacion= QtWidgets.QApplication([])
ventanap= uic.loadUi("ventanavista.ui")
consultar()
ventanap.show()
#consultar()

ventanap.tblContactos.setHorizontalHeaderLabels(['Codigo','Producto','Cantidad','Valor','Cedula'])
ventanap.tblContactos.setEditTriggers(QTableWidget.NoEditTriggers)
ventanap.tblContactos.setSelectionBehavior(QTableWidget.SelectRows)

ventanap.tblContactos.cellClicked.connect(seleccionar)

ventanap.btnAgregar.clicked.connect(agregar)
ventanap.btnEliminar.clicked.connect(eliminar)
ventanap.btnModificar.clicked.connect(modificar)
ventanap.btnCancelar.clicked.connect(cancelar)

sys.exit(aplicacion.exec())