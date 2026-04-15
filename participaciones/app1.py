import sqlite3
conn = sqlite3.connect("instituto.db"  )    
conn.execute(
    """CREATE TABLE if not exists cursos (
        id INTEGER PRIMARY KEY,
        descripcion TEXT,
        horas INTEGER NOT NULL
    )"""
)

conn.execute(
    """
    create table if not exists estudiantes (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        fecha_nacimiento TEXT NOT NULL
    )
    """
)

conn.execute (
    """
    create table if not exists incripciones(
        id INTEGER PRIMARY KEY,
        fecha_inscripcion TEXT NOT NULL,
        curso_id INTEGER NOT NULL,
        estudiante_id INTEGER NOT NULL,
        FOREIGN KEY (curso_id) REFERENCES cursos(id),
        FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id)

    )
    """
)

# conn.execute(
#     """
#     insert into cursos (descripcion, horas)
#     values ("TECNOLOGIAS EMERGENTES II ", 40)
#     """
# )

# conn.execute(
#     """
#     insert into estudiantes (nombre, apellido, fecha_nacimiento)
#     values ("ARACELY", "PUCHO", "2005-05-27")
#     """
# )   
# conn.commit()

conn.execute(
    """
    insert into incripciones (fecha_inscripcion, curso_id, estudiante_id)
    values ("2024-03-01", 2, 1)
    """
)

conn.commit()

print("\nCURSOS:")
cursor = conn.execute("select * from cursos")
for fila in cursor:
    print(fila)
    
print("\nESTUDIANTES:")
cursor = conn.execute("select * from estudiantes")
for fila in cursor:
    print(fila)

print("\nINSCRIPCIONES:")
cursor = conn.execute("select * from incripciones")
for fila in cursor:
    print(fila)

# print("\nCURSOS:")
# curso = conn.execute("select * from cursos")
# for c in curso:
#     print(c)