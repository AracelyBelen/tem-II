from flask import render_template
from flask import request
from flask import redirect

from app.productos import bp_productos

from app.models.producto import Producto

from app import db

# LISTAR
@bp_productos.route('/')
def listar_productos():

    productos = Producto.query.all()

    return render_template(

        'productos/listar.html',

        productos=productos

    )

# AGREGAR
@bp_productos.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():

    if request.method == 'POST':

        nombre = request.form['nombre']

        precio = request.form['precio']

        stock = request.form['stock']

        nuevo_producto = Producto(

            nombre=nombre,

            precio=precio,

            stock=stock

        )

        db.session.add(nuevo_producto)

        db.session.commit()

        return redirect('/productos')

    return render_template(

        'productos/agregar.html'
    )

# EDITAR
@bp_productos.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):

    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':

        producto.nombre = request.form['nombre']

        producto.precio = request.form['precio']

        producto.stock = request.form['stock']

        db.session.commit()

        return redirect('/productos')

    return render_template(

        'productos/editar.html',

        producto=producto

    )

# ELIMINAR
@bp_productos.route('/eliminar/<int:id>')
def eliminar_producto(id):

    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)

    db.session.commit()

    return redirect('/productos')