import sqlite3

def crear_db():
    conexion = sqlite3.connect('citas.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pacientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mascota TEXT NOT NULL,
            propietario TEXT NOT NULL,
            especie TEXT,
            fecha TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente")


if __name__ == "__main__":
    crear_db()