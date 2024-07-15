from flask import Flask, render_template, url_for, request, jsonify
import numpy as np
from base.MyConnection import * 
from MyFile import *
from Final import *

app = Flask(__name__,static_folder='static')
conn = MyConnection.connect()
final = Final(conn)

@app.route('/')
def lasa():
    final.graphe.afficher()
    return render_template('index.html',ips = final.file.ip,sites = final.file.site,i=0)

@app.route("/couper", methods=['POST'])
def couper():
    tab = request.get_json()
    final.couper(tab[0],tab[1])
    return jsonify(tab)

@app.route("/search", methods=['POST'])
def trouver():
    tab = request.get_json()
    final.trouver(tab[0],tab[1])
    return jsonify(tab)