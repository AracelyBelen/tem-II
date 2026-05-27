from flask import render_template
from flask import request
from flask import redirect
from app.clientes import bp_clientes
from app.models.cliente import Cliente
from app import db
import re
# LISTAR
@bp_clientes.route('/')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template(
        'clientes/listar.html',
        clientes=clientes
    )
# AGREGAR
@bp_clientes.route('/agregar', methods=['GET', 'POST'])
def agregar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', nombre):
            return "Nombre inválido"
        # VALIDAR TELÉFONO
        if not telefono.isdigit():
            return "Teléfono inválido"
        nuevo_cliente = Cliente(
            nombre=nombre,
            telefono=telefono
        )
        db.session.add(nuevo_cliente)
        db.session.commit()
        return redirect('/clientes')
    return render_template(
        'clientes/agregar.html'
    )
# EDITAR
@bp_clientes.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nombre = request.form['nombre']
        cliente.telefono = request.form['telefono']
        if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$', cliente.nombre):
            return "Nombre inválido"
        if not cliente.telefono.isdigit():
            return "Teléfono inválido"
        db.session.commit()
        return redirect('/clientes')
    return render_template(
        'clientes/editar.html',
        cliente=cliente
    )
# ELIMINAR
@bp_clientes.route('/eliminar/<int:id>')
def eliminar_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect('/clientes')