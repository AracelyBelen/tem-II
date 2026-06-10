from flask import Flask
from flask import jsonify
from flask import request

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///peliculas.db"

db = SQLAlchemy(app)

class Pelicula(db.Model):

    __tablename__ = "peliculas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(100),
        nullable=False
    )

    genero = db.Column(
        db.String(50),
        nullable=False
    )

    calificacion = db.Column(
        db.Float,
        nullable=False
    )
with app.app_context():
    db.create_all()
    
@app.route("/")
def inicio():
    return {"mensaje":"API REST de Peliculas funcionando"}
    
@app.route("/peliculas")
def obtener_peliculas():

    peliculas = Pelicula.query.all()

    resultado = []

    for pelicula in peliculas:

        resultado.append({

            "id": pelicula.id,

            "titulo": pelicula.titulo,

            "genero": pelicula.genero,

            "calificacion": pelicula.calificacion

        })

    return jsonify(resultado)

@app.route("/peliculas",methods=["POST"])
def agregar_pelicula():

    datos = request.get_json()
    if not datos["titulo"].strip():
        return jsonify({"error":"El titulo es obligatorio"}), 400

    if not datos["genero"].strip():
        return jsonify({"error":"El genero es obligatorio"}), 400

    if datos["calificacion"] < 0 or datos["calificacion"] > 10:
        return jsonify({"error":"La calificacion debe estar entre 0 y 10"}), 400
    nueva = Pelicula(

        titulo=datos["titulo"],

        genero=datos["genero"],

        calificacion=datos["calificacion"]

    )
    db.session.add(nueva)
    db.session.commit()
    return jsonify({"mensaje":"Pelicula agregada"})
    
@app.route("/peliculas/<int:id>")
def obtener_pelicula(id):

    pelicula = Pelicula.query.get_or_404(id)

    return jsonify({

        "id": pelicula.id,

        "titulo": pelicula.titulo,

        "genero": pelicula.genero,

        "calificacion": pelicula.calificacion

    })
    
@app.route("/peliculas/<int:id>",methods=["PUT"])
def actualizar_pelicula(id):

    pelicula = Pelicula.query.get_or_404(id)

    datos = request.get_json()
    if not datos["titulo"].strip():
        return jsonify({"error":"El titulo es obligatorio"}), 400

    if not datos["genero"].strip():
        return jsonify({"error":"El genero es obligatorio"}), 400

    if datos["calificacion"] < 0 or datos["calificacion"] > 10:
        return jsonify({"error":"La calificacion debe estar entre 0 y 10"}), 400

    pelicula.titulo = datos["titulo"]
    pelicula.genero = datos["genero"]
    pelicula.calificacion = datos["calificacion"]
    db.session.commit()
    return jsonify({"mensaje":"Pelicula actualizada"})
    
@app.route("/peliculas/<int:id>", methods=["DELETE"])
def eliminar_pelicula(id):

    pelicula = Pelicula.query.get_or_404(id)

    db.session.delete(pelicula)

    db.session.commit()

    return jsonify({
        "mensaje":"Pelicula eliminada"
    })
    
if __name__ == "__main__":
    app.run(debug=True)