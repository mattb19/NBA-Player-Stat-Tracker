from flask import Flask, redirect, url_for, render_template
from flask_cors import CORS
from WebScraper import *

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})




@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/shark", methods=["GET"])
def MsByrdDipped():
    return "shark"