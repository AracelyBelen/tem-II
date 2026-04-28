from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/styles.css')
def estilos():
    return send_from_directory('templates', 'styles.css')

@app.route('/script.js')
def script():
    return send_from_directory('templates', 'script.js')

@app.route('/img/<path:filename>')
def imagenes(filename):
    return send_from_directory('img', filename)

if __name__ == '__main__':
    app.run(debug=True)