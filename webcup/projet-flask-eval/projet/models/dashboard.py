from projet.db import db

class V_board(db.Model):
    __tablename__ = 'v_board'
    __table_args__ = {'info': dict(is_view=True)}

    total = db.Column(db.Float(precision=2), primary_key=True) 
    paye = db.Column(db.Float(precision=2)) 
    reste = db.Column(db.Float(precision=2))


class Histogramme(db.Model):
    __tablename__ = 'histogramme'
    __table_args__ = {'info': dict(is_view=True)}

    ligne = db.Column(db.Integer, primary_key=True) 
    annee = db.Column(db.Integer) 
    moi = db.Column(db.Integer) 
    libelle = db.Column(db.String) 
    montant = db.Column(db.Float)
    


