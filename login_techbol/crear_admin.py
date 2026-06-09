from app import create_app
from app.extensions import db, bcrypt
from app.models.usuario import Usuario

app = create_app()

with app.app_context():

    existe = Usuario.query.filter_by(
        username="admin"
    ).first()

    if not existe:

        admin = Usuario(
            username="admin",
            password=bcrypt.generate_password_hash(
                "123456"
            ).decode("utf-8"),
            rol="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Administrador creado")

    else:

        print("Ya existe")