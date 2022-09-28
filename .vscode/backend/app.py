from flask import Flask, redirect, url_for, request
from flask_cors import CORS
from WebScraper import *
from flask import jsonify
from Player import Player
from PostAvg import PostAvg
from CareerAvg import CareerAvg
from RegAvg import RegAvg
from ComparePlayers import Comparison
from PlayerList import PlayerList

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})




Mike = RegAvg("Michael", "Jordan", 50, 23, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
Steph = RegAvg("Steph", "Curry", 60, 69, 20, 15, 17, 15, 13, 9, 2, 8, 10, 7, 6, 5)
LeBron = RegAvg("LeBron", "James", 72, 12, 30, 18, 11, 18, 13, 9, 3, 8, 10, 1, 6, 8)
players = [Mike, Steph, LeBron]
newPlayerList = PlayerList()
newPlayerList.setPlayerList(players)
playerList = newPlayerList.getPlayerList()

# GET Route Handler
@app.route("/playerstats", methods=['GET', 'POST'])
def playerstats():
    return jsonify({
        "stats" : playerList,
        "status" : "success"
    })

@app.route("/")
def home():
    return redirect(url_for("playerstats"))