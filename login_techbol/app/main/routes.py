from flask import Blueprint
from flask import render_template
from app.models.cliente import Cliente
from app.models.producto import Producto
from app.models.pedido import Pedido
from flask_login import login_required

main_bp = Blueprint(
    "main",
    __name__
)

@main_bp.route("/inicio")
@login_required
def index():
    total_clientes = Cliente.query.count()
    total_productos = Producto.query.count()
    total_pedidos = Pedido.query.count()

    return render_template(
        "main/index.html",
        total_clientes=total_clientes,
        total_productos=total_productos,
        total_pedidos=total_pedidos
    )