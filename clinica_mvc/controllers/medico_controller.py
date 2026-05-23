from clinica import app, db
from flask import render_template, request, redirect
from models.medico import Medico
import re

@app.route('/')
def index():
    return render_template('index.html')

# LISTAR
@app.route('/medicos')
def listar_medicos():

    medicos = Medico.query.all()

    return render_template(
        'medicos/listar.html',
        medicos=medicos
    )

# AGREGAR
@app.route('/medicos/agregar', methods=['GET', 'POST'])
def agregar_medico():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']
        # VALIDAR SOLO LETRAS
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', nombre):
            return 'El nombre solo debe tener letras'
        # VALIDAR TELEFONO
        if not telefono.isdigit():
            return 'El telefono solo debe tener numeros'
        nuevo_medico = Medico(
            nombre=nombre,
            especialidad=especialidad,
            telefono=telefono,
            correo=correo
        )
        db.session.add(nuevo_medico)
        db.session.commit()
        return redirect('/medicos')
    return render_template('medicos/agregar.html')

# EDITAR
@app.route('/medicos/editar/<int:id>')
def editar_medico(id):

    medico = Medico.query.get(id)

    return render_template(
        'medicos/editar.html',
        medico=medico
    )

@app.route('/medicos/actualizar/<int:id>', methods=['POST'])
def actualizar_medico(id):

    medico = Medico.query.get(id)

    medico.nombre = request.form['nombre']
    medico.especialidad = request.form['especialidad']
    medico.telefono = request.form['telefono']
    medico.correo = request.form['correo']

    db.session.commit()

    return redirect('/medicos')

# ELIMINAR
@app.route('/medicos/eliminar/<int:id>')
def eliminar_medico(id):

    medico = Medico.query.get(id)

    db.session.delete(medico)

    db.session.commit()

    return redirect('/medicos')