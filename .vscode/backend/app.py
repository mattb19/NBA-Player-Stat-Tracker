from flask import Flask, redirect, url_for, render_template
from flask_cors import CORS
from WebScraper import *

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*':{'origins': 'http://localhost:8080', "allow_headers" : "Access-Control-Allow-Origin"}})

players = ["player1", "player2", "player3", "player4"]

@app.route("/yep", methods=["GET"])
def main():
    return players