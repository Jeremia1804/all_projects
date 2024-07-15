from projet import app
from flask import render_template, redirect, url_for, session, request, make_response, jsonify
from projet.annotation.authentication import auth
from projet.models.finition import FinitionModel
from projet.models.maison import MaisonModel
from projet.services.service_devis import insert_devis, paiement_devis, getTravauxDevis
from projet.services.service_session import getMyId
from projet.annotation.authentication import auth
from projet.models.devis import DevisModel, V_devis
from flask_weasyprint import HTML
from projet.models.paiement import PaiementModel

@app.route('/client', methods = ['GET'])
@auth('CLIENT')
def indexclient():
    id = getMyId()
    nombre = V_devis.query.filter(V_devis.idclient==id).count()
    url = "/getmydevis"
    return render_template('page/client/index.html', url=url, nb = nombre)

@app.route('/create-devis', methods = ['GET'])
@auth('CLIENT')
def createdevispage():
    finition = FinitionModel.find_all()    
    maison = MaisonModel.find_all()
    for m in maison:
        m.repareDescription() 
    return render_template('page/client/create_devis.html', maison=maison, finition=finition)

@app.route('/insert-devis', methods = ['POST'])
@auth('CLIENT')
def createdevis():
    date = request.form['datedebut']
    lieu = request.form['lieu']
    idmaison = int(request.form['idmaison'])
    idfinition = int(request.form['idfinition'])
    id = getMyId()
    try:
        insert_devis(id,idmaison,idfinition,date,lieu)
        return redirect(url_for('indexclient'))
    except Exception as e:
        return {'message':str(e)}


@app.route('/payer-devis', methods = ['POST'])
@auth('CLIENT')
def paiementdevis():
    date = request.form['date']
    iddevis = int(request.form['iddevis'])
    montant = float(request.form['montant'])
    try:
        paiement_devis(iddevis,montant,date)
        return {'message':'Payement reussi avec succes'}, 200
    except Exception as e:
        return {'error':str(e)}, 500

@app.route('/paiement', methods = ['GET'])
@auth('CLIENT')
def paiement():
    id = getMyId()
    devis  = DevisModel.find_by_idClient(id)
    return render_template('page/client/paiement.html', devis = devis)

@app.route('/getmydevis', methods = ['POST'])
@auth('CLIENT')
def getmydevis():
    form = request.form
    size = int(form.get('size'))
    page = int(form.get('page'))
    tri_col = form.get('tri')

    if tri_col == 'null' or tri_col=='undefined':
        tri_col = 'iddevis'
    colonne_tri = getattr(V_devis, tri_col)
    id = getMyId()
    requete = V_devis.query.filter(V_devis.idclient==id)
    requete = requete.order_by(colonne_tri.asc()).paginate(page=page, per_page=size)
    return {'data':[req.json() for req in requete]}, 200

@app.route('/export-pdf/<int:id>', methods = ['GET','POST'])
def export_pdf(id):
    devis = V_devis.query.filter(V_devis.iddevis==id).first()
    paiement  = PaiementModel.query.filter(PaiementModel.iddevis==id)
    total_paiement = 0
    for p in paiement:
        total_paiement = total_paiement + p.montant
    travaux = getTravauxDevis(id)
    html_content = render_template('page/monpdf.html', travaux=travaux, total = devis.total, paiement = paiement, total_p = total_paiement, devis=devis)
    pdf = HTML(string=html_content).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachement; filename=example.pdf'
    return response

@app.route('/vision-pdf/<int:id>', methods = ['GET','POST'])
def vision_pdf(id):
    devis = V_devis.query.filter(V_devis.iddevis==id).first()
    paiement  = PaiementModel.query.filter(PaiementModel.iddevis==id)
    total_paiement = 0
    for p in paiement:
        total_paiement = total_paiement + p.montant
    travaux = getTravauxDevis(id)
    html_content = render_template('page/monpdf.html', travaux=travaux, total = devis.total, paiement = paiement, total_p = total_paiement, devis=devis)
    pdf = HTML(string=html_content).write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=example.pdf'
    return response