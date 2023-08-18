import sys
import pyodbc
conn= pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\ASUS\Documents\GitHub\pruebas acces\Database1.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM persona")
for row in cursor.fetchall():
    print(row)
cursor.close
conn.close