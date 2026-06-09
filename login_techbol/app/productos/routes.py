from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from app.extensions import db
from app.models.producto import Producto

productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos"
)


@productos_bp.route("/")
@login_required
def listar_productos():

    productos = Producto.query.all()

    return render_template(
        "productos/listar.html",
        productos=productos
    )


@productos_bp.route("/agregar", methods=["GET", "POST"])
@login_required
def agregar_producto():

    if request.method == "POST":

        nombre = request.form["nombre"].strip()
        precio = request.form["precio"]
        stock = request.form["stock"]

        try:

            precio = float(precio)
            stock = int(stock)

        except:

            flash(
                "Precio o stock inválidos",
                "danger"
            )

            return redirect(
                url_for(
                    "productos.agregar_producto"
                )
            )

        if precio <= 0:

            flash(
                "El precio debe ser mayor a 0",
                "danger"
            )

            return redirect(
                url_for(
                    "productos.agregar_producto"
                )
            )

        if stock < 0:

            flash(
                "Stock inválido",
                "danger"
            )

            return redirect(
                url_for(
                    "productos.agregar_producto"
                )
            )

        nuevo_producto = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock
        )

        db.session.add(
            nuevo_producto
        )

        db.session.commit()

        flash(
            "Producto agregado correctamente",
            "success"
        )

        return redirect(
            url_for(
                "productos.listar_productos"
            )
        )

    return render_template(
        "productos/agregar.html"
    )


@productos_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_producto(id):

    producto = Producto.query.get_or_404(id)

    if request.method == "POST":

        producto.nombre = request.form["nombre"]

        producto.precio = float(
            request.form["precio"]
        )

        producto.stock = int(
            request.form["stock"]
        )

        db.session.commit()

        flash(
            "Producto actualizado",
            "success"
        )

        return redirect(
            url_for(
                "productos.listar_productos"
            )
        )

    return render_template(
        "productos/editar.html",
        producto=producto
    )


@productos_bp.route("/eliminar/<int:id>")
@login_required
def eliminar_producto(id):

    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)

    db.session.commit()

    flash(
        "Producto eliminado",
        "warning"
    )

    return redirect(
        url_for(
            "productos.listar_productos"
        )
    )