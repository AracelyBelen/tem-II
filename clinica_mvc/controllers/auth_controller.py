from clinica import app, db
from flask import render_template, request, redirect, session

from models.usuario import Usuario

@app.route('/registro', methods=['GET', 'POST'])
def registro():

    if request.method == 'POST':

        nuevo_usuario = Usuario(
            usuario=request.form['usuario'],
            password=request.form['password']
        )

        db.session.add(nuevo_usuario)

        db.session.commit()

        return redirect('/login')

    return render_template('auth/registro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        usuario = request.form['usuario']
        password = request.form['password']

        usuario_encontrado = Usuario.query.filter_by(
            usuario=usuario,
            password=password
        ).first()

        if usuario_encontrado:

            session['usuario'] = usuario

            return redirect('/')

    return render_template('auth/login.html')

@app.route('/logout')
def logout():

    session.clear()

    return redirect('/login')