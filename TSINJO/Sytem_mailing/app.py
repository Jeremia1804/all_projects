from flask import Flask, request,render_template,url_for,jsonify,json,session,redirect
from datetime import timedelta
from classes.Gestion import *
from classes.Verification import *
from classes.base.MyConnection import *
from classes.Analyse import *
from classes.Cryptography import *

app = Flask(__name__)


app.secret_key = '06112003'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

conn = MyConnection.connect()
lessessions = {}
analyse = Analyse()
crypt = Cryptography()

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('verslogin'))
    else:
        return redirect(url_for('boitereception'))

@app.route('/verslogin')
def verslogin():
    if 'user' in session:
        return redirect(url_for('boitereception'))
    return render_template('page-login.html')


#page pour afficher
@app.route('/boitereception')
def boitereception():
    if 'user' in session:
        lessessions[str(session['user']['id'])].actualiser()
        boitereceptions = lessessions[str(session['user']['id'])].getBoiteReception()
        return render_template('boitereception.html',boite = boitereceptions)
    return redirect(url_for('verslogin'))

@app.route('/newmessage')
def newmessage():
    if 'user' in session:
        return render_template('newmessage.html')
    return redirect(url_for('verslogin'))

@app.route('/lire')
def lire():
    if 'user' in session:
        id = request.args.get('idmail')
        val = lessessions[str(session['user']['id'])].verifierMail(int(id))
        if val == True:
            lessessions[str(session['user']['id'])].insertIsRead(int(id),1)
        lessessions[str(session['user']['id'])].actualiser()
        mail = lessessions[str(session['user']['id'])].getMailById(int(id))
        return render_template('lire.html',mail = mail,compte=session['user']['compte'])
    return redirect(url_for('verslogin'))

@app.route('/spamite')
def spamite():
    if 'user' in session:
        id = request.args.get('idmail')
        val = request.args.get('valeur')
        lessessions[str(session['user']['id'])].insertIsSpam(int(id),str(val))
        lessessions[str(session['user']['id'])].nb +=1
        if lessessions[str(session['user']['id'])].nb == 10:
            return redirect(url_for('actualiser'))
        return redirect(url_for('lire',idmail=id))
    return redirect(url_for('verslogin'))

@app.route('/envoye')
def envoye():
    if 'user' in session:
        lessessions[str(session['user']['id'])].actualiser()
        envoyes = lessessions[str(session['user']['id'])].getEnvoyes()
        return render_template('envoye.html',envoyes = envoyes)
    return redirect(url_for('verslogin'))

@app.route('/spam')
def spam():
    if 'user' in session:
        lessessions[str(session['user']['id'])].actualiser()
        spams = lessessions[str(session['user']['id'])].getSpam()
        return render_template('spam.html',spams = spams)
    return redirect(url_for('verslogin'))
#fin page pour afficher

@app.route('/login', methods=['POST'])
def login():
    mail = request.form.get('mail')
    mdp = request.form.get('pass')
    valeur = check(conn,mail,mdp)
    if valeur != False:
        lessessions[str(valeur.utilisateur.id)] =  valeur
        session['user'] = valeur.utilisateur.toJson()
        return redirect(url_for('boitereception'))
    return redirect(url_for('verslogin'))


@app.route('/envoi', methods=['POST'])
def envoi():
    texte = request.form.get('texte')
    spam = analyse.prediction(texte)
    objet = request.form.get('objet')
    texte_chiffre = crypt.encrypt_AES(texte)
    texte = texte_chiffre.hex()
    texte = texte.replace("'","''")
    objet = objet.replace("'","''")
    compte = request.form.get('compteDestinataire')
    lessessions[str(session['user']['id'])].envoiMail(objet,texte,compte,spam)
    return redirect(url_for('envoye'))

@app.route('/repondre', methods=['POST'])
def repondre():
    texte = request.form.get('texte')
    spam = analyse.prediction(texte)
    texte = texte.replace("'","''")
    idMere = request.form.get('idmail')
    mailMere = lessessions[str(session['user']['id'])].getMailById(int(idMere))
    if mailMere == None:
        return redirect(url_for('boitereception'))
    else:
        lessessions[str(session['user']['id'])].repondre(mailMere,texte,spam)
        return redirect(url_for('envoye'))

@app.route('/actualiser')
def actualiser():
    analyse.renouveller(conn)
    return redirect(url_for('boitereception'))

@app.route('/logout')
def logout():
    lessessions.pop(str(session['user']['id']))
    session.clear()
    return redirect(url_for('index'))

@app.route('/suggestion', methods=['POST'])
def suggestion():
    mot = request.form.get('mot')
    tab = ["liantsoa","jeremia","sergio"]
    return jsonify(tab)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
