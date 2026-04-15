from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# CONEXIÓN BD
def get_db():
    conn = sqlite3.connect("kardex.db")
    conn.row_factory = sqlite3.Row
    return conn

# CREAR TABLA
def init_db():
    conn = get_db()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS personas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        telefono TEXT,
        fecha_nac TEXT
    )
    """)
    conn.commit()
    conn.close()

init_db()

# LISTAR
@app.route("/")
def index():
    conn = get_db()
    personas = conn.execute("SELECT * FROM personas").fetchall()
    conn.close()
    return render_template("index.html", personas=personas)

# CREATE
@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        fecha_nac = request.form["fecha_nac"]

        conn = get_db()
        conn.execute(
            "INSERT INTO personas (nombre, telefono, fecha_nac) VALUES (?, ?, ?)",
            (nombre, telefono, fecha_nac)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("create.html")

# UPDATE
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    conn = get_db()

    if request.method == "POST":
        nombre = request.form["nombre"]
        telefono = request.form["telefono"]
        fecha_nac = request.form["fecha_nac"]

        conn.execute(
            "UPDATE personas SET nombre=?, telefono=?, fecha_nac=? WHERE id=?",
            (nombre, telefono, fecha_nac, id)
        )
        conn.commit()
        conn.close()

        return redirect("/")

    persona = conn.execute("SELECT * FROM personas WHERE id=?", (id,)).fetchone()
    conn.close()

    return render_template("edit.html", persona=persona)

# DELETE
@app.route("/delete/<int:id>")
def delete(id):
    conn = get_db()
    conn.execute("DELETE FROM personas WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return redirect("/")

# EJECUTAR
if __name__ == "__main__":
    app.run(debug=True)