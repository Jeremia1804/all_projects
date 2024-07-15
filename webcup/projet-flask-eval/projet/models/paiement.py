from projet.db import db

class PaiementModel(db.Model):
    __tablename__ = 'paiement'
    
    idpaiement = db.Column(db.Integer, primary_key=True)
    iddevis = db.Column(db.Integer, db.ForeignKey('devis.iddevis'))
    montant = db.Column(db.Float)
    dateheure = db.Column(db.Date)
    reference = db.Column(db.String)
    
    devis = db.relationship("DevisModel")

    def __init__(self, iddevis, montant, dateheure, reference):
        self.iddevis = iddevis
        self.montant = montant
        self.dateheure = dateheure
        self.reference = reference

    def json(self):
        return {
            'idpaiement': self.idpaiement,
            'iddevis': self.iddevis,
            'montant': self.montant,
            'dateheure': self.dateheure.isoformat() if self.dateheure else None,
            'reference':self.reference
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
