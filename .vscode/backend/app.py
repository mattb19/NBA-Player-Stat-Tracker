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




# Mike = RegAvg("Michael", "Jordan", 50, 23, 'nuggets', 'pf', 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
# Steph = RegAvg("Steph", "Curry", 60, 69, 'pistons', 'pf', 20, 15, 17, 15, 13, 9, 2, 8, 10, 7, 6, 5)
# LeBron = RegAvg("LeBron", "James", 72, 12, 'warriors', 'pf', 30, 18, 11, 18, 13, 9, 3, 8, 22, 1, 6, 8)
# Kev = RegAvg("Kevin", "Durant", 74, 74, 'rockets', 'pf', 30, 67, 77, 72, 73, 1, 3, 7, 50, 7, 9, 7)
# Kev1 = RegAvg("Kevin", "Durant", 74, 74, 'pacers', 'pf', 30, 67, 77, 72, 73, 1, 3, 7, 50, 7, 9, 7)
# Kev2 = RegAvg("Kevin", "Durant", 74, 74, 'clippers', 'pf', 30, 67, 77, 72, 73, 1, 3, 7, 50, 7, 9, 7)
# Kev3 = RegAvg("Kevin", "Durant", 74, 74, 'grizzlies', 'pf', 30, 67, 77, 72, 73, 1, 3, 7, 50, 7, 9, 7)
# Kev4 = RegAvg("Kevin", "Durant", 74, 74, 'heat', 'pf', 30, 67, 77, 72, 73, 1, 3, 7, 50, 7, 9, 7)
# players = [Mike, Steph, LeBron, Kev, Kev1, Kev2, Kev3, Kev4]
# newPlayerList = PlayerList()
# newPlayerList.setPlayerList(players)
# playerList = newPlayerList.getPlayerList()

# newComparison = Comparison(Mike, LeBron)
# comparison = newComparison.getComparison()
kev = WebScraper().getData("Kevin Durant")
steph = WebScraper().getData("Stephen Curry")

players = [kev, steph]
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

@app.route("/compare", methods=['GET', 'POST'])
def compare():
    return jsonify({
        "comparison" : comparison,
        "status" : "success"
    })

@app.route("/")
def home():
    return redirect(url_for("playerstats"))