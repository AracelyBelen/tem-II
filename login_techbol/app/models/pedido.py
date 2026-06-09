from app.extensions import db

class Pedido(db.Model):

    __tablename__ = "pedidos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    cantidad = db.Column(
        db.Integer,
        nullable=False
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey("productos.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Pedido {self.id}>"