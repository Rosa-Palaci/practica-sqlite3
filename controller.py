import sqlite3 as sql

def createDb():
    conn =sql.connect("estudiantes.db")
    conn.commit()
    conn.close()

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
    #createDb()
    createTable()