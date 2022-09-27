from flask import Flask, redirect, url_for, render_template
from flask_cors import CORS
from WebScraper import *
from flask import jsonify

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})

stats = [
    {
        'player':'Mike Jordan',
        'wl':'100%',
        'ppg':100.2
    },
    {
        'player':'Steph Curry',
        'wl':'99%',
        'ppg':0.2
    },
    {
        'player':'Gianny',
        'wl':'50%',
        'ppg':2.2
    },
    {
        'player':'Lebron Jame',
        'wl':'1%',
        'ppg':0.1
    }
]

# GET Route Handler
@app.route("/playerstats", methods=['GET'])
def playerstats():
    return jsonify({
        "stats" : stats,
        "status" : "success"
    })


@app.route("/")
def home():
    return redirect(url_for("playerstats"))