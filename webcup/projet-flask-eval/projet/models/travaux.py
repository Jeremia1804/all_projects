from projet.db import db


class TravauxModel(db.Model):
    __tablename__ = 'travaux'
    
    idtravaux= db.Column(db.Integer, primary_key=True)
    libelle=db.Column(db.String)
    unite=db.Column(db.String)
    pu=db.Column(db.Float)
    code = db.Column(db.String)

    def __init__(self, libelle, unite, pu, code):
        self.libelle = libelle
        self.unite = unite
        self.pu = pu
        self.code = code

    def json(self):
        return {
        'id': self.idtravaux,
        'libelle': self.libelle,
        'unite': self.unite,
        'pu': self.pu,
        'code': self.code
    }

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idtravaux=id).first()
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def setPuAndQuantite(self, pu,quantite):
        self.pu = pu
        self.quantite = quantite
        self.montant = pu*quantite