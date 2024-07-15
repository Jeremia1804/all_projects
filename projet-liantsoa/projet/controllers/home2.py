from projet import app
from flask import render_template, redirect, url_for


@app.route('/home2', methods = ['GET'])
def index2():
    return render_template('inc/body2.html')

