from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')


# 🔹 Ruta para CSS
@app.route('/styles.css')
def estilos():
    return send_from_directory('templates', 'styles.css')


# 🔹 Ruta para JS
@app.route('/script.js')
def script():
    return send_from_directory('templates', 'script.js')


# 🔹 Ruta para imágenes
@app.route('/img/<path:filename>')
def imagenes(filename):
    return send_from_directory('img', filename)


if __name__ == '__main__':
    app.run(debug=True)