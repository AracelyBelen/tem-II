from flask import Flask, render_template, request, redirect, send_from_directory
from datetime import date
import sqlite3
import re

app = Flask(__name__)

@app.route('/styles.css')
def estilos():
    return send_from_directory('templates', 'styles.css')

@app.route('/img/<path:filename>')
def imagenes(filename):
    return send_from_directory('img', filename)

@app.route('/')
def index():
    conexion = sqlite3.connect('citas.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM pacientes")
    citas = cursor.fetchall()
    conexion.close()

    return render_template('index.html', citas=citas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    hoy = date.today().isoformat()

    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']
        patron = "^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$"

        if not re.match(patron, mascota):
            return render_template('agregar.html', error="Mascota inválida (solo letras)", fecha_hoy=hoy)

        if not re.match(patron, propietario):
            return render_template('agregar.html', error="Propietario inválido (solo letras)", fecha_hoy=hoy)

        if especie and not re.match(patron, especie):
            return render_template('agregar.html', error="Especie inválida (solo letras)", fecha_hoy=hoy)

        if fecha < hoy:
            return render_template('agregar.html', error="No se permiten fechas pasadas", fecha_hoy=hoy)

        conexion = sqlite3.connect('citas.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO pacientes (mascota, propietario, especie, fecha)VALUES (?, ?, ?, ?)''', (mascota, propietario, especie, fecha))
        conexion.commit()
        conexion.close()
        return redirect('/')

    return render_template('agregar.html', fecha_hoy=hoy)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conexion = sqlite3.connect('citas.db')
    cursor = conexion.cursor()
    hoy = date.today().isoformat()

    if request.method == 'POST':
        mascota = request.form['mascota']
        propietario = request.form['propietario']
        especie = request.form['especie']
        fecha = request.form['fecha']
        patron = "^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$"

        if not re.match(patron, mascota):
            return render_template('editar.html', error="Mascota inválida", cita=(id, mascota, propietario, especie, fecha))

        if not re.match(patron, propietario):
            return render_template('editar.html', error="Propietario inválido", cita=(id, mascota, propietario, especie, fecha))

        if especie and not re.match(patron, especie):
            return render_template('editar.html', error="Especie inválida", cita=(id, mascota, propietario, especie, fecha))

        if fecha < hoy:
            return render_template('editar.html', error="Fecha inválida", cita=(id, mascota, propietario, especie, fecha))

        # Actualizar BD
        cursor.execute('''
            UPDATE pacientes
            SET mascota=?, propietario=?, especie=?, fecha=?
            WHERE id=?
        ''', (mascota, propietario, especie, fecha, id))

        conexion.commit()
        conexion.close()
        return redirect('/')

    cursor.execute("SELECT * FROM pacientes WHERE id=?", (id,))
    cita = cursor.fetchone()
    conexion.close()

    return render_template('editar.html', cita=cita)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    conexion = sqlite3.connect('citas.db')
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM pacientes WHERE id=?", (id,))
    conexion.commit()
    conexion.close()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)