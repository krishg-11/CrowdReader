from flask import Flask, render_template
from test import getFrequency

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/application.html")
def application():
    return render_template("application.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/description.html")
def description():
    return render_template("description.html")

@app.route("/image.html")
def image():
    test = getFrequency("C:/Users/4euge/Downloads/download")
    mx = max(test)
    return render_template("image.html", test=test, mx=mx)

if __name__ == "__main__":
    app.run(debug=True)
