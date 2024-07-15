from flask import Flask, render_template, url_for, request, jsonify
import numpy as np
from PIL import Image
import os
import io
import base64
from Gestion import *

app = Flask(__name__,static_folder='static')
gestion = None

@app.route('/')
def index():
    return render_template('first.html')

@app.route('/jouer', methods=['GET'])
def jouer():
    global gestion
    photo = request.args.get('photo')
    chemin_image = os.path.join(app.static_folder, 'img', f'{photo}.jpg')
    image = Image.open(chemin_image)
    gestion = Gestion(image)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('jeu.html',photo=image_base64)


@app.route("/diviser", methods=['POST'])
def diviser():
    data = request.json
    larg = int(data.get('larg'))
    hauteur = int(data.get('hauteur'))
    global gestion
    gestion.diviser(larg,hauteur)
    return jsonify(gestion.getNoeuds())

@app.route("/bouger", methods=['POST'])
def bouger():
    data = request.json
    data1 = data.get('data1')
    data2 = data.get('data2')
    data1 = data1.split(";")
    data2 = data2.split(";")
    x1 = int(data1[0])
    x2 = int(data2[0])
    y1 = int(data1[1])
    y2 = int(data2[1])
    global gestion
    valiny = gestion.manakisaka(x1,y1,x2,y2)
    data = {
        "noeuds":gestion.getNoeuds(),
        "etat" :valiny
    }
    return jsonify(data)

@app.route("/melanger", methods=['POST'])
def melanger():
    global gestion 
    gestion.melanger()
    return jsonify(gestion.getNoeuds())

@app.route("/rotate", methods=['POST'])
def rotate():
    data = request.json
    deg = int(data.get('degre'))
    global gestion 
    gestion.manodina(deg)
    # print(str(rep)+" dehhhhhhhhh")
    return jsonify(gestion.getNoeuds())



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
