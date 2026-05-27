from app import db

class Pedido(db.Model):

    __tablename__ = 'pedidos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha = db.Column(
        db.String(20),
        nullable=False
    )

    monto = db.Column(
        db.Float,
        nullable=False
    )

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey('productos.id')
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.id')
    )

    producto = db.relationship(

        'Producto',

        backref='pedidos'
    )