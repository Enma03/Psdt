
import mysql.connector

print ("Resultados de mysql.connector:")
miConexion = mysql.connector.connect(host='127.0.0.1', user='root', passwd='', db='prueba1')
cur = miConexion.cursor()
cur.execute("SELECT Nombre FROM Asignatura")
for nombre in cur.fetchall():
    print (nombre)
miConexion.close()