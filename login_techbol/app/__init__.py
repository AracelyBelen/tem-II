from flask import Flask
from app.auth import auth_bp
from app.config import Config
from app.clientes import clientes_bp
from app.extensions import (db,migrate,bcrypt,login_manager)
from app.models.usuario import Usuario
from app.productos import productos_bp
from app.pedidos import pedidos_bp
from app.main import main_bp

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    from app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(productos_bp)
    app.register_blueprint(pedidos_bp)
    app.register_blueprint(main_bp)

    return app

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))