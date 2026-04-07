from flask import Flask, render_template
import feedparser

app = Flask(__name__)

@app.route("/")
def home():
    url = "http://feeds.bbci.co.uk/mundo/rss.xml"
    feed = feedparser.parse(url)
    noticias = feed.entries[:5]
    return render_template("index4.html", noticias=noticias)

if __name__ == "__main__":
    app.run(debug=True)