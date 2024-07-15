from projet import app
from flask import render_template, redirect, url_for, session, request, make_response, jsonify
from projet.annotation.authentication import auth
from projet.models.devis import V_devis
from projet.models.dashboard import V_board, Histogramme
from projet.services.service_devis import getTravauxDevis
from projet.models.finition import FinitionModel
from projet.models.travaux import TravauxModel
from projet.services.importcsv import import_first, import_second
from projet.services.fonction import delete_all_data

@app.route('/dashboard', methods = ['GET'])
def dashboard():
    board = V_board.query.first()
    return render_template('page/admin/dashboard.html', board=board)

@app.route('/liste-devis', methods = ['GET'])
def devis_list():
    devis = V_devis.query.all()
    nombre = V_devis.query.count()
    url = "/getalldevis"
    return render_template('page/admin/devis.html', url=url, nb=nombre, devis = devis)

@app.route('/detail-devis/<int:id>', methods = ['GET'])
def devis_detail(id):
    devis = V_devis.query.filter(V_devis.iddevis==id).first()
    travaux = getTravauxDevis(id)
    return render_template('page/admin/detail-devis.html', devis = devis, travaux = travaux)


@app.route('/getalldevis', methods = ['POST'])
def getalldevis():
    form = request.form
    size = int(form.get('size'))
    page = int(form.get('page'))
    tri_col = form.get('tri')

    if tri_col == 'null' or tri_col=='undefined':
        tri_col = 'iddevis'

    colonne_tri = getattr(V_devis, tri_col)
    requete = V_devis.query.order_by(colonne_tri.asc()).paginate(page=page, per_page=size)
    return {'data':[req.json() for req in requete]}, 200

@app.route('/getdatahisto', methods = ['POST'])
def getdatahisto():
    form = request.form
    annee = int(form.get('year'))

    data = Histogramme.query.filter(Histogramme.annee==annee)
    lib = []
    val = []
    for d in data:
        lib.append(d.libelle)
        val.append(d.montant)
    return {'libelle':lib, 'valeur':val}, 200


@app.route('/finition', methods = ['GET'])
def pagefinition():
    finitions = FinitionModel.find_all()
    return render_template('page/admin/finition.html', finitions = finitions)

@app.route('/page-import', methods = ['GET'])
def page_import():
    return render_template('page/admin/import.html')

@app.route('/form-update-finition/<int:id>', methods = ['GET'])
def form_update(id):
    finition = FinitionModel.find_by_id(id);
    return render_template('page/admin/form-update-finition.html', finition = finition)

@app.route('/finition/update', methods = ['POST'])
def update_finition():
    form = request.form
    idfinition = int(form.get('idfinition'))
    libelle = form.get('libelle')
    augmentation = float(form.get('augmentation'))
    finition = FinitionModel.find_by_id(idfinition);

    finition.libelle = libelle
    finition.augmentation = augmentation
    finition.save_to_db()
    return redirect(url_for('pagefinition'))


@app.route('/travaux', methods = ['GET'])
def pagetravaux():
    travaux = TravauxModel.find_all()
    return render_template('page/admin/travaux.html', travaux = travaux)

@app.route('/form-update-travaux/<int:id>', methods = ['GET'])
def form_update_travaux(id):
    travaux = TravauxModel.find_by_id(id);
    return render_template('page/admin/form-update-travaux.html', travaux = travaux)

@app.route('/travaux/update', methods = ['POST'])
def update_travaux():
    form = request.form
    idtravaux = int(form.get('idtravaux'))
    libelle = form.get('libelle')
    pu = float(form.get('pu'))
    code = form.get('code')
    unite = form.get('unite')
    travaux = TravauxModel.find_by_id(idtravaux);

    travaux.libelle = libelle
    travaux.pu = pu
    travaux.code = code
    travaux.unite = unite
    travaux.save_to_db()
    return redirect(url_for('pagetravaux'))


@app.route('/importer-travaux', methods = ['POST'])
def import_travaux():
    if 'travaux' not in request.files or 'devis' not in request.files:
        return {'message':'Fichier manquant'}
    
    travaux = request.files['travaux']
    devis = request.files['devis']
    
    trav = "projet/uploads/" + travaux.filename
    dev = "projet/uploads/" + devis.filename
    import_first(trav,dev)

    return redirect(url_for('pagefinition'))

@app.route('/importer-paiement', methods = ['POST'])
def import_paiement():
    if 'paiement' not in request.files:
        return {'message':'Fichier manquant'}
    
    paiement = request.files['paiement']
    
    paye = "projet/uploads/" + paiement.filename
    import_second(paye)
    return redirect(url_for('pagefinition'))

from projet.models.detailDevis import DetailDevisModel
from projet.models.paiement import PaiementModel
from projet.models.devis import DevisModel
from projet.models.maisontravaux import MaisonTravauxModel
from projet.models.maison import MaisonModel
from projet.models.travaux import TravauxModel
from projet.models.finition import FinitionModel

@app.route('/delete-data', methods = ['GET'])
def deletealldata():
    delete_all_data(DetailDevisModel,PaiementModel,DevisModel, MaisonTravauxModel, TravauxModel,FinitionModel, MaisonModel)
    return redirect(url_for('dashboard'))