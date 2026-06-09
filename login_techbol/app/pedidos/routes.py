from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from app.extensions import db

from app.models.pedido import Pedido
from app.models.cliente import Cliente
from app.models.producto import Producto

pedidos_bp = Blueprint(
    "pedidos",
    __name__,
    url_prefix="/pedidos"
)


@pedidos_bp.route("/")
@login_required
def listar_pedidos():

    pedidos = Pedido.query.all()

    return render_template(
        "pedidos/listar.html",
        pedidos=pedidos
    )


@pedidos_bp.route("/agregar", methods=["GET", "POST"])
@login_required
def agregar_pedido():

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":

        cliente_id = request.form["cliente_id"]
        producto_id = request.form["producto_id"]
        cantidad = int(request.form["cantidad"])

        producto = Producto.query.get(producto_id)

        if cantidad <= 0:

            flash(
                "Cantidad inválida",
                "danger"
            )

            return redirect(
                url_for(
                    "pedidos.agregar_pedido"
                )
            )

        if cantidad > producto.stock:

            flash(
                "Stock insuficiente",
                "danger"
            )

            return redirect(
                url_for(
                    "pedidos.agregar_pedido"
                )
            )

        producto.stock -= cantidad

        pedido = Pedido(
            cliente_id=cliente_id,
            producto_id=producto_id,
            cantidad=cantidad
        )

        db.session.add(pedido)

        db.session.commit()

        flash(
            "Pedido registrado",
            "success"
        )

        return redirect(
            url_for(
                "pedidos.listar_pedidos"
            )
        )

    return render_template(
        "pedidos/agregar.html",
        clientes=clientes,
        productos=productos
    )
    
@pedidos_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_pedido(id):

    pedido = Pedido.query.get_or_404(id)

    clientes = Cliente.query.all()
    productos = Producto.query.all()

    if request.method == "POST":

        nueva_cantidad = int(request.form["cantidad"])

        producto = Producto.query.get(
            pedido.producto_id
        )

        # devolver stock anterior
        producto.stock += pedido.cantidad

        # verificar nuevo stock
        if nueva_cantidad > producto.stock:

            flash(
                "Stock insuficiente",
                "danger"
            )

            return redirect(
                url_for(
                    "pedidos.editar_pedido",
                    id=id
                )
            )

        # descontar stock nuevo
        producto.stock -= nueva_cantidad

        pedido.cliente_id = request.form["cliente_id"]
        pedido.producto_id = request.form["producto_id"]
        pedido.cantidad = nueva_cantidad

        db.session.commit()

        flash(
            "Pedido actualizado",
            "success"
        )

        return redirect(
            url_for(
                "pedidos.listar_pedidos"
            )
        )

    return render_template(
        "pedidos/editar.html",
        pedido=pedido,
        clientes=clientes,
        productos=productos
    )


@pedidos_bp.route("/eliminar/<int:id>")
@login_required
def eliminar_pedido(id):

    pedido = Pedido.query.get_or_404(id)

    producto = Producto.query.get(
        pedido.producto_id
    )

    producto.stock += pedido.cantidad

    db.session.delete(pedido)

    db.session.commit()

    flash(
        "Pedido eliminado",
        "warning"
    )

    return redirect(
        url_for(
            "pedidos.listar_pedidos"
        )
    )