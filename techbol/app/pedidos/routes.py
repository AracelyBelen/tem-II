from flask import render_template
from flask import request
from flask import redirect

from app.pedidos import bp_pedidos

from app.models.pedido import Pedido
from app.models.producto import Producto
from app.models.cliente import Cliente

from app import db

# LISTAR
@bp_pedidos.route('/')
def listar_pedidos():

    pedidos = Pedido.query.all()

    return render_template(

        'pedidos/listar.html',

        pedidos=pedidos

    )

# AGREGAR
@bp_pedidos.route('/agregar', methods=['GET', 'POST'])
def agregar_pedido():

    productos = Producto.query.all()

    clientes = Cliente.query.all()

    if request.method == 'POST':

        fecha = request.form['fecha']

        monto = request.form['monto']

        producto_id = request.form['producto_id']

        cliente_id = request.form['cliente_id']

        nuevo_pedido = Pedido(

            fecha=fecha,

            monto=monto,

            producto_id=producto_id,

            cliente_id=cliente_id

        )

        db.session.add(nuevo_pedido)

        db.session.commit()

        return redirect('/pedidos')

    return render_template(

        'pedidos/agregar.html',

        productos=productos,

        clientes=clientes

    )

# EDITAR
@bp_pedidos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_pedido(id):

    pedido = Pedido.query.get_or_404(id)

    productos = Producto.query.all()

    clientes = Cliente.query.all()

    if request.method == 'POST':

        pedido.fecha = request.form['fecha']

        pedido.monto = request.form['monto']

        pedido.producto_id = request.form['producto_id']

        pedido.cliente_id = request.form['cliente_id']

        db.session.commit()

        return redirect('/pedidos')

    return render_template(

        'pedidos/editar.html',

        pedido=pedido,

        productos=productos,

        clientes=clientes

    )

# ELIMINAR
@bp_pedidos.route('/eliminar/<int:id>')
def eliminar_pedido(id):

    pedido = Pedido.query.get_or_404(id)

    db.session.delete(pedido)

    db.session.commit()

    return redirect('/pedidos')