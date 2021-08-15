import sqlite3
from sqlite3.dbapi2 import connect

class productos:
    def iniciarConexion(self):
        conexion=sqlite3.connect('Base.s3db')
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion
     
    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="SELECT * FROM Productos"
        cursor.execute(sentencialSQL)
        return cursor.fetchall()
    
    def crearContacto(self, datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="INSERT INTO Productos(Cod_prod,Producto,Cantidad,Valor,Cedula) VALUES(?,?,?,?,?)"
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()
        
    def borrarContacto(self, cedulaContactos):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="DELETE FROM Productos WHERE Cedula=(?)"
        cursor.execute(sentencialSQL,[cedulaContactos])
        conexion.commit()
        conexion.close()
        
    def modificarContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="UPDATE Productos SET Producto=? ,Cantidad=? ,Valor=? ,Cedula=? WHERE Cod_prod=?"
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()