from flask import Flask, render_template, url_for, request, jsonify
from Final import *
import numpy as np

app = Flask(__name__,static_folder='static')

@app.route('/')
def lasa():
    return render_template('taquin.html')

@app.route("/resolution", methods=['POST'])
def afficher():
    matrice = request.get_json()
    file = Final(np.array(matrice))
    valiny = file.preparer()
    chemin = file.chemin(valiny)
    print(chemin)
    return jsonify(chemin)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
