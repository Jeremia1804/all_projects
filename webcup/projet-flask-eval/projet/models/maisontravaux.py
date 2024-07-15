from projet.db import db

class MaisonTravauxModel(db.Model):
    __tablename__ = 'maisontravaux'
    
    idmaisontravaux = db.Column(db.Integer, primary_key=True)
    idmaison = db.Column(db.Integer, db.ForeignKey('maison.idmaison'))
    idtravaux = db.Column(db.Integer, db.ForeignKey('travaux.idtravaux'))
    quantite = db.Column(db.Float)
    dateheure = db.Column(db.TIMESTAMP)  # Gardé en TIMESTAMP
    
    maison = db.relationship("MaisonModel")
    travaux = db.relationship("TravauxModel")

    def __init__(self, idmaison, idtravaux, quantite, dateheure):
        self.idmaison = idmaison
        self.idtravaux = idtravaux
        self.quantite = quantite
        self.dateheure = dateheure

    def json(self):
        return {
            'idmaisontravaux': self.idmaisontravaux,
            'idmaison': self.idmaison,
            'idtravaux': self.idtravaux,
            'quantite': self.quantite,
            'dateheure': self.dateheure.isoformat() if self.dateheure else None
        }

    @classmethod
    def find_by_id(cls, idmaison):
        return cls.query.filter_by(idmaison=idmaison).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
