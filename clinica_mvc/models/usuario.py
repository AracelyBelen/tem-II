from clinica import db

class Usuario(db.Model):

    __tablename__ = 'usuarios'

    id_usuario = db.Column(
        db.Integer,
        primary_key=True
    )

    usuario = db.Column(
        db.String(50),
        nullable=False
    )

    password = db.Column(
        db.String(100),
        nullable=False
    )