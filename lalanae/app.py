from flask import Flask, render_template,url_for
from object.LalanaSimba import *
from base.MyConnection import *
from affichage.Map import *

app = Flask(__name__)


@app.route('/')
def index():
    conn = MyConnection.connect()
    data_Map = Map()
    map_content = []
    map_content.append(data_Map.getMap()) 
    suivant = "<table border='1'><tr><th>IdLalana</th><th>Niveau</th><th>Prix</th><th>Duree</th></tr>"
    cout = LalanaSimba.getAllSimba(conn)
    rep = LalanaSimba.triParCout(cout,conn)
    for row in rep:
        suivant += "<tr><td>"+str(row.getIdLalana())+"</td><td>"+str(row.getNiveau())+"</td><td>"+str(row.getCoutP())+"</td><td>"+str(row.getCoutD())+"</td></tr>"
    suivant += "</table>"
    map_content.append(suivant)
    return render_template('index.html', map=map_content)
