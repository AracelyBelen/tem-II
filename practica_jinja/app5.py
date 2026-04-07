from flask import Flask, render_template
import feedparser
app = Flask(__name__)
FUENTES = {
    "bbc": {
        "nombre": "BBC Mundo",
        "url": "http://feeds.bbci.co.uk/mundo/rss.xml"
    },
    "elpais": {
        "nombre": "El Pais",
        "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada"
    }
}
@app.route("/")
def index():
    return render_template("index5.html", fuentes=FUENTES)

@app.route("/noticias/<fuente_id>")
def mostrar_noticias(fuente_id):
    fuente = FUENTES.get(fuente_id)
    feed = feedparser.parse(fuente["url"])
    noticias = feed.entries[:5]
    return render_template("noticias.html",fuente=fuente, noticias=noticias)

if __name__ == "__main__":
    app.run(debug=True)