import mysql.connector

try:
    print("Attempting to connect to MySQL server...")
    miConexion = mysql.connector.connect(
        host='localhost',  # Update if necessary
        user='root',       # Update with your MySQL username
        passwd='123456',         # Update with your MySQL password
        db='prueba1'
    )

    print("Connected to MySQL server")
    
    cur = miConexion.cursor()
    cur.execute("SELECT Nombre FROM Asignatura")
    
    print("Results from the query:")
    for nombre in cur.fetchall():
        print(nombre)
    
    miConexion.close()
    
except mysql.connector.Error as err:
    print("Error:", err)
