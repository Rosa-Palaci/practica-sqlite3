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

def insertRowEstudiantes(idEstudiante, numero_lista, grupo, genero, ciclo_escolar):
    conn =sql.connect("estudiantes.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO estudiantes  VALUES({idEstudiante}, {numero_lista}, '{grupo}', '{genero}','{ciclo_escolar}')"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def readRowEstudiantes():
    conn =sql.connect("estudiantes.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM estudiantes"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

def insertRowsEstudiantes(estudiantesLista):
    conn =sql.connect("estudiantes.db")
    cursor = conn.cursor()
    instruccion = f"INSERT INTO estudiantes  VALUES(?, ?, ?, ?, ?)"
    cursor.executemany(instruccion, estudiantesLista)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn =sql.connect("estudiantes.db")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM estudiantes ORDER BY {field}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print(datos)

if __name__ == "__main__":
    #createDb()
    #createTable()
    #insertRowEstudiantes(1, 1, "A", "Femenino", "2023-2024")
    #insertRowEstudiantes(2, 2, "A", "Masculino", "2023-2024")
    #readRowEstudiantes()
    estudiantes = {
        (3, 3, "A", "Masculino", "2023-2024"),
        (4, 4, "A", "Femenino", "2023-2024"),
        (5, 5, "A", "Masculino", "2023-2024")
    }
    #insertRowsEstudiantes(estudiantes)
    readOrdered("genero")