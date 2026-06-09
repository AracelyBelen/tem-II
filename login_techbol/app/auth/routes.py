from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from app.extensions import db
from app.extensions import bcrypt

from app.models.usuario import Usuario

import re

auth_bp = Blueprint(
    "auth",
    __name__
)

@auth_bp.route("/")
def inicio():

    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"].strip()

        usuario = Usuario.query.filter_by(
            username=username
        ).first()

        if usuario and bcrypt.check_password_hash(
            usuario.password,
            password
        ):

            login_user(usuario)

            flash(
                "Bienvenido al sistema",
                "success"
            )

            return redirect(
                url_for(
                    "main.index"
                )
            )

        flash(
            "Usuario o contraseña incorrectos",
            "danger"
        )

    return render_template(
        "auth/login.html"
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()

        password = request.form["password"].strip()

        rol = request.form["rol"]

        if not re.match(
            r'^[A-Za-z0-9_]+$',
            username
        ):

            flash(
                "Usuario inválido",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        if len(password) < 6:

            flash(
                "La contraseña debe tener al menos 6 caracteres",
                "danger"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        existe = Usuario.query.filter_by(
            username=username
        ).first()

        if existe:

            flash(
                "El usuario ya existe",
                "warning"
            )

            return redirect(
                url_for(
                    "auth.register"
                )
            )

        password_hash = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        nuevo_usuario = Usuario(

            username=username,

            password=password_hash,

            rol=rol

        )

        db.session.add(
            nuevo_usuario
        )

        db.session.commit()

        flash(
            "Usuario registrado correctamente",
            "success"
        )

        return redirect(
            url_for(
                "auth.login"
            )
        )

    return render_template(
        "auth/register.html"
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Sesión cerrada",
        "info"
    )

    return redirect(
        url_for(
            "auth.login"
        )
    )