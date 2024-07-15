from projet import app
from flask import render_template, redirect, url_for
from projet.models.Personne import *
from projet.services.importe import *

@app.route('/', methods = ['GET'])
def index():
    data = []
    for p in Personne.find_all():
        data.append(p.json())
    return render_template("pages/body.html")

# @app.route('/save', methods = ['GET'])
# def save():
#     p = Personne.find_all()[0]
#     p.name = "Jeremia"
#     p.save_to_db()
#     return redirect(url_for('index'))

@app.route('/importer_donnees', methods=['GET'])
def importer_donnees():
    cond, donnee = import_fichier('D:/eval/projet-flask-eval/donnees-import.xlsx')
    if cond:
        return {'message':'le fichier a ete importe'}
    else:
        return {'errors':donnee}