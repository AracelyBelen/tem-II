from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_required

from app.extensions import db
from app.models.cliente import Cliente

import re

clientes_bp = Blueprint(
    "clientes",
    __name__,
    url_prefix="/clientes"
)


@clientes_bp.route("/")
@login_required
def listar_clientes():

    clientes = Cliente.query.all()

    return render_template(
        "clientes/listar.html",
        clientes=clientes
    )


@clientes_bp.route("/agregar", methods=["GET", "POST"])
@login_required
def agregar_cliente():

    if request.method == "POST":

        nombre = request.form["nombre"].strip()
        telefono = request.form["telefono"].strip()
        direccion = request.form["direccion"].strip()

        if not re.match(
            r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$',
            nombre
        ):
            flash(
                "El nombre solo debe contener letras",
                "danger"
            )
            return redirect(
                url_for("clientes.agregar_cliente")
            )

        if not telefono.isdigit():
            flash(
                "El teléfono solo debe contener números",
                "danger"
            )
            return redirect(
                url_for("clientes.agregar_cliente")
            )

        nuevo_cliente = Cliente(
            nombre=nombre,
            telefono=telefono,
            direccion=direccion
        )

        db.session.add(nuevo_cliente)
        db.session.commit()

        flash(
            "Cliente agregado correctamente",
            "success"
        )

        return redirect(
            url_for("clientes.listar_clientes")
        )

    return render_template(
        "clientes/agregar.html"
    )


@clientes_bp.route("/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    if request.method == "POST":

        nombre = request.form["nombre"].strip()
        telefono = request.form["telefono"].strip()
        direccion = request.form["direccion"].strip()

        if not re.match(
            r'^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$',
            nombre
        ):
            flash(
                "Nombre inválido",
                "danger"
            )
            return redirect(
                url_for(
                    "clientes.editar_cliente",
                    id=id
                )
            )

        if not telefono.isdigit():
            flash(
                "Teléfono inválido",
                "danger"
            )
            return redirect(
                url_for(
                    "clientes.editar_cliente",
                    id=id
                )
            )

        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.direccion = direccion

        db.session.commit()

        flash(
            "Cliente actualizado",
            "success"
        )

        return redirect(
            url_for("clientes.listar_clientes")
        )

    return render_template(
        "clientes/editar.html",
        cliente=cliente
    )


@clientes_bp.route("/eliminar/<int:id>")
@login_required
def eliminar_cliente(id):

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)

    db.session.commit()

    flash(
        "Cliente eliminado",
        "warning"
    )

    return redirect(
        url_for("clientes.listar_clientes")
    )