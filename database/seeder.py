import sqlite3 as sql

DB_PATH = "C:\Users\palac\OneDrive\Escritorio\practica-sqlites3\database\estudiantes.db"

def createTableEstudiantes():
    conn =sql.connect("estudiantes.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE estudiantes(
            idEstudiante INTEGER PRIMARY KEY,
            numero_lista INTEGER,
            grupo VARCHAR,
            genero VARCHAR,
            ciclo_escolar VARCHAR
        )
        """      
    )
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print("Holaaa")