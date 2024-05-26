import sqlite3 as sql

def createDb():
    conn =sql.connect("estudiantes.db")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    createDb()