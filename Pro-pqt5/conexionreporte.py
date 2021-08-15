import sqlite3
from sqlite3.dbapi2 import connect

class reporte:
    def iniciarConexion(self):
        conexion=sqlite3.connect('Base.s3db')
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion
     
    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="SELECT * FROM vista_tablas"
        cursor.execute(sentencialSQL)
        return cursor.fetchall()
    
    def leerContactosReporte(self):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="SELECT * FROM vista_tablas"
        cursor.execute(sentencialSQL)
        resultado=cursor.fetchall()
        for registro in resultado:
            Cedula= registro[0]
            Nombre= registro[1]
            Apellido = registro[2]
            Telefono = registro[3]
            Correo = registro[4]
            Codigo = registro[5]
            Producto = registro[6]
            Cantidad = registro[7]
            Valor = registro[8]
            print ("Cedula=%s, Nombre==%s, Apellido=%s, Telefono=%s, Correo=%s, Codigo=%s, Producto=%s, Cantidad=%s, Valor=%s")
        conexion.close()     
'''    
    def crearContacto(self, datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="INSERT INTO contactos(Cedula,nombre,apellido,telefono,correo) VALUES(?,?,?,?,?)"
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()
        
    def borrarContacto(self, cedulaContactos):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="DELETE FROM contactos WHERE cedula=(?)"
        cursor.execute(sentencialSQL,[cedulaContactos])
        conexion.commit()
        conexion.close()
        
    def modificarContacto(self,datosContacto):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="UPDATE contactos SET nombre=? ,apellido=? ,telefono=? ,correo=? WHERE cedula=?"
        cursor.execute(sentencialSQL,datosContacto)
        conexion.commit()
        conexion.close()'''