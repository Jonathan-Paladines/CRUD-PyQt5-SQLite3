import sqlite3

try:
    bd = sqlite3.connect('Base.s3db')
    cursor = bd.cursor()
    senetencia = "SELECT * FROM vista_tablas"
    
    cursor.execute(senetencia)
    
    archivo = cursor.fetchall()
    
    print ("Base de Datos Abierta")

except sqlite3.OperationalError as error:
    print("Error al Abrir", error)
    

archivo_reporte=open("Reporte.txt","w")
print(archivo)
archivo_reporte.write(str(archivo))
archivo_reporte.close()    