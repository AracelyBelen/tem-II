from clinica import app, db
from flask import render_template, request, redirect

from models.consulta import Consulta
from models.medico import Medico
from models.paciente import Paciente

@app.route('/consultas')
def listar_consultas():

    consultas = Consulta.query.all()

    return render_template(
        'consultas/listar.html',
        consultas=consultas
    )

@app.route('/consultas/agregar', methods=['GET', 'POST'])
def agregar_consulta():

    medicos = Medico.query.all()
    pacientes = Paciente.query.all()

    if request.method == 'POST':

        nueva_consulta = Consulta(
            fecha=request.form['fecha'],
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )

        db.session.add(nueva_consulta)

        db.session.commit()

        return redirect('/consultas')

    return render_template(
        'consultas/agregar.html',
        medicos=medicos,
        pacientes=pacientes
    )
    
@app.route('/consultas/editar/<int:id>')
def editar_consulta(id):
    consulta = Consulta.query.get(id)
    medicos = Medico.query.all()
    pacientes = Paciente.query.all()
    return render_template(
        'consultas/editar.html',
        consulta=consulta,
        medicos=medicos,
        pacientes=pacientes
    )
    
@app.route('/consultas/actualizar/<int:id>',methods=['POST'])
def actualizar_consulta(id):
    consulta = Consulta.query.get(id)
    consulta.fecha = request.form['fecha']
    consulta.diagnostico = request.form['diagnostico']
    consulta.tratamiento = request.form['tratamiento']
    consulta.id_medico = request.form['id_medico']
    consulta.id_paciente = request.form['id_paciente']
    db.session.commit()
    return redirect('/consultas')

@app.route('/consultas/eliminar/<int:id>')
def eliminar_consulta(id):
    consulta = Consulta.query.get(id)
    db.session.delete(consulta)
    db.session.commit()
    return redirect('/consultas')