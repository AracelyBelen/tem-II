from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/proceso",methods=["POST"])
def proceso():
    nombre = request.form.get("nombre")
    
    lenguajes = request.form.getlist
    return render_template("salida.html", nombre = nombre, lenguajes = lenguajes)


    
if __name__ == "__main__":
    app.run(debug=True)