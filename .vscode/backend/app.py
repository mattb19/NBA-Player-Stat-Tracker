from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from WebScraper import *
from flask import jsonify

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})

stats = [
    {
        'team':'../assets/bulls.png',
        'player':'Mike Jordan',
        'age':'50',
        'number':'23',
        'gp':'10',
        'min':'10',
        'fgpercent':'10',
        'threeptpercent':'10',
        'ftpercent':'10',
        'reb':'10',
        'ast':'10',
        'blk':'10',
        'stl':'10',
        'pf':'10',
        'to':'10',
        'pts':'10',
    },
    {
        'team':'../assets/lakers.png',
        'player':'Lebrabra Jame',
        'age':'100',
        'number':'69',
        'gp':'10',
        'min':'10',
        'fgpercent':'10',
        'threeptpercent':'10',
        'ftpercent':'10',
        'reb':'10',
        'ast':'10',
        'blk':'10',
        'stl':'10',
        'pf':'10',
        'to':'10',
        'pts':'10',
    }
]

# GET Route Handler
@app.route("/playerstats", methods=['GET', 'POST'])
def playerstats():
    return jsonify({
        "stats" : stats,
        "status" : "success"
    })

@app.route("/")
def home():
    return redirect(url_for("playerstats"))