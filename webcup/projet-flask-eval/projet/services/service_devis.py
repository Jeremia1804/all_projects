from projet.db import db
from projet.models.maison import MaisonModel
from projet.models.finition import FinitionModel
from projet.models.devis import DevisModel
from projet.services.fonction import getDateActuelle
from projet.models.maisontravaux import MaisonTravauxModel
from projet.models.travaux import TravauxModel
from projet.models.detailDevis import DetailDevisModel
from projet.models.paiement import PaiementModel
from projet.models.devis import V_devis

def insert_devis(id,idmaison,idfinition,datedebut, lieu):
    try:
        maison = MaisonModel.find_by_id(idmaison)
        finition = FinitionModel.find_by_id(idfinition)
        devis = DevisModel(idmaison,idfinition,id,datedebut,getDateActuelle(),finition.augmentation,maison.duree,"D002",lieu)
        devis.save_to_db()
        db.session.flush()
        maisonTravaux = MaisonTravauxModel.find_by_id(idmaison)
        insert_detaildevis(maisonTravaux,devis.iddevis)
        db.session.commit()
    except Exception as e:
        raise e

def insert_detaildevis(maisontravaux,iddevis):
    for maison in maisontravaux:
        travaux = TravauxModel.find_by_id(maison.idtravaux)
        detail = DetailDevisModel(iddevis,maison.idtravaux,maison.quantite,travaux.pu)
        detail.save_to_db()


def paiement_devis(iddevis, montant, date):
    devis = V_devis.query.filter(V_devis.iddevis==iddevis).first()
    if devis.reste < montant:
        raise Exception("Le montant que vous avez entrez est trop grande, il vous reste "+str(devis.reste)+" Ar a paye")
    paiement = PaiementModel(iddevis,montant, date, "P002")
    paiement.save_to_db()


def getTravauxDevis(iddevis):
    details = DetailDevisModel.find_by_idDevis(iddevis)
    travaux = []
    for det in details:
        tr = TravauxModel.find_by_id(det.idtravaux)
        tr.setPuAndQuantite(det.pu,det.quantite)
        travaux.append(tr)
    return travaux