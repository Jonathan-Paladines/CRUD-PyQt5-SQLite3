import sqlite3
from sqlite3.dbapi2 import connect

class contactos:
    def iniciarConexion(self):
        conexion=sqlite3.connect('Base.s3db')
        conexion.text_factory = lambda b: b.decode(errors='ignore')
        return conexion
     
    def leerContactos(self):
        conexion=self.iniciarConexion()
        cursor= conexion.cursor()
        sentencialSQL="SELECT * FROM contactos"
        cursor.execute(sentencialSQL)
        return cursor.fetchall()
    
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
        conexion.close()