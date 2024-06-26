import sqlite3 as sql


DB_PATH = "C:\\Users\\palac\\OneDrive\\Escritorio\\practica-sqlites3\\database\\estudiantes.db"

def createTableEstudiantes():
    conn =sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE estudiantes(
            id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
            numero_lista INTEGER,
            grupo VARCHAR,
            genero VARCHAR,
            ciclo_escolar VARCHAR
        )
        """      
    )
    conn.commit()
    conn.close()

def addValuesEstudiantes():
    conn =sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        (0, 1, "A", "Masculino", "2023-2024"),
        (1, 2, "A", "Femenino", "2023-2024"),
        (2, 3, "A", "Masculino", "2023-2024")
    ]
    cursor.executemany("""INSERT INTO estudiantes VALUES(?, ?, ?, ?, ?)""", data)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createTableEstudiantes()
    addValuesEstudiantes()