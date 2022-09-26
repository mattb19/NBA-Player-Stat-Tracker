from flask import Flask, redirect, url_for, render_template
from WebScraper import *

app = Flask(__name__)
isAdmin = False

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/noHax")
def noHax():
    return "<h1>YOU WOULDA THOUGHT <h1>"

@app.route("/admin")
def admin():
    if isAdmin == False:
        return redirect(url_for("noHax"))
    else:
        return redirect(url_for("home"))