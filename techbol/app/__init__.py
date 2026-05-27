from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()
migrate = Migrate()
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    # INICIALIZAR DB
    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.cliente import Cliente
    from app.models.producto import Producto
    from app.models.pedido import Pedido
    # IMPORTAR BLUEPRINTS
    from app.clientes.routes import bp_clientes
    from app.productos.routes import bp_productos
    from app.pedidos.routes import bp_pedidos
    # REGISTRAR BLUEPRINTS
    app.register_blueprint(
        bp_clientes,
        url_prefix='/clientes'
    )
    app.register_blueprint(
        bp_productos,
        url_prefix='/productos'
    )
    app.register_blueprint(
        bp_pedidos,
        url_prefix='/pedidos'
    )
    @app.route('/')
    def inicio():
        return render_template('base.html')
    return app