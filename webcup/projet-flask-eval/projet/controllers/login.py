from projet.models.admin import AdminModel
from projet import app
from flask import render_template, redirect, url_for, session, request, make_response, jsonify

@app.route('/auth/login', methods = ['GET'])
def login_admin():
    return render_template('page/admin/login_auth.html')

@app.route('/login', methods = ['GET'])
def login_client():
    return render_template('page/client/login_client.html')

@app.route('/seconnecter', methods = ['POST'])
def connexclient():
    num = request.form['num']
    session['user'] = {'num': num, 'roles': ['CLIENT']}
    return redirect(url_for('indexclient'))

@app.route('/auth/seconnecter', methods = ['POST'])
def connexadmin():
    email = request.form['email']
    password = request.form['password']
    print(password)
    admin = AdminModel.query.filter_by(email=email).one_or_none()
    if not admin or not admin.check_password(password):
        return redirect(url_for('login_admin'))
        
    session['user'] = {'num': 'tout', 'roles': ['ADMIN']}
    return redirect(url_for('dashboard'))

@app.route('/logout', methods = ['GET'])
def logout():
    session.clear()
    return redirect(url_for('login_client'))