from flask import Flask, redirect, url_for
from WebScraper import *
from playerlist.py import *

app = Flask(__name__)

@app.route("/")
def home():
    yes = WebScraper.youaregay()
    return yes