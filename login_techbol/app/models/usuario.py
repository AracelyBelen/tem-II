from app.extensions import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(255),
        nullable=False
    )

    rol = db.Column(
        db.String(20),
        nullable=False,
        default="vendedor"
    )

    def __repr__(self):
        return f"<Usuario {self.username}>"