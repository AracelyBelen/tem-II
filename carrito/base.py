import sqlite3

def crear_db():
    conexion = sqlite3.connect('tienda.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            imagen TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()
    print("Base de datos lista")


# Ejecutar solo para crear la estructura
if __name__ == "__main__":
    crear_db()