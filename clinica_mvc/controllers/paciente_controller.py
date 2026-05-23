from clinica import app, db
from flask import render_template, request, redirect
from models.paciente import Paciente
import re

@app.route('/pacientes')
def listar_pacientes():

    pacientes = Paciente.query.all()

    return render_template(
        'pacientes/listar.html',
        pacientes=pacientes
    )
    
@app.route('/pacientes/editar/<int:id>')
def editar_paciente(id):
    paciente = Paciente.query.get(id)
    return render_template(
        'pacientes/editar.html',
        paciente=paciente
    )
    
@app.route('/pacientes/actualizar/<int:id>',methods=['POST'])
def actualizar_paciente(id):
    paciente = Paciente.query.get(id)
    paciente.nombre = request.form['nombre']
    paciente.edad = request.form['edad']
    paciente.direccion = request.form['direccion']
    paciente.telefono = request.form['telefono']
    db.session.commit()
    return redirect('/pacientes')

@app.route('/pacientes/agregar', methods=['GET', 'POST'])
def agregar_paciente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', nombre):
            return 'El nombre solo debe contener letras'
        if not edad.isdigit():
            return 'La edad solo debe contener numeros'
        if not telefono.isdigit():
            return 'El telefono solo debe contener numeros'
        nuevo_paciente = Paciente(
            nombre=nombre,
            edad=edad,
            direccion=direccion,
            telefono=telefono
        )
        db.session.add(nuevo_paciente)
        db.session.commit()
        return redirect('/pacientes')
    return render_template('pacientes/agregar.html')

@app.route('/pacientes/eliminar/<int:id>')
def eliminar_paciente(id):

    paciente = Paciente.query.get(id)

    db.session.delete(paciente)

    db.session.commit()

    return redirect('/pacientes')