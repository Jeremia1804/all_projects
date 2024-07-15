from flask import Flask, render_template, url_for, request, jsonify
from Affichage import *

app = Flask(__name__)

@app.route('/')
def lasa():
    rep = Affichage.afficherLalasimbaParCout(5000)
    res = Affichage.afficherLalanaRN(5000)
    return render_template('affiche.html',seho=rep,seho1 = res)

@app.route("/changer", methods=['GET'])
def afficher():
    nb = request.args.get("Nom")
    rep = Affichage.afficherLalasimbaParCout(nb)
    res = Affichage.afficherLalanaRN(nb)
    return render_template('affiche.html',seho=rep,seho1 = res)