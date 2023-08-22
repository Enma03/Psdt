import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ASUS\Documents\GitHub\buenas practicas\Psdt\pruebas acces\Database1.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM AsgEst ORDER BY id ASC")
print("(ID, 'NOTA1', 'NOTA2', 'NOTA3', 'idAsignatura', 'idEstudiante', 'FECHA')")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close