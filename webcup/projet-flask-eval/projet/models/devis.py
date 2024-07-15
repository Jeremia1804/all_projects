from projet.db import db

class DevisModel(db.Model):
    __tablename__ = 'devis'
    
    iddevis = db.Column(db.Integer, primary_key=True)
    reference = db.Column(db.String)
    idmaison = db.Column(db.Integer, db.ForeignKey('maison.idmaison'))
    idfinition = db.Column(db.Integer, db.ForeignKey('finition.idfinition'))
    idclient = db.Column(db.String)
    debuttravaux = db.Column(db.Date) 
    datedevis = db.Column(db.Date)  # Nouvelle colonne
    augmentation = db.Column(db.Float)
    duree = db.Column(db.Float)
    lieu  = db.Column(db.String)
    
    maison = db.relationship("MaisonModel")
    finition = db.relationship("FinitionModel")

    def __init__(self, idmaison, idfinition, idclient, debuttravaux, datedevis, augmentation, duree,reference,lieu):
        self.idmaison = idmaison
        self.idfinition = idfinition
        self.idclient = idclient
        self.debuttravaux = debuttravaux
        self.datedevis = datedevis
        self.augmentation = augmentation
        self.duree = duree
        self.reference = reference
        self.lieu = lieu

    def json(self):
        return {
            'iddevis': self.iddevis,
            'idmaison': self.idmaison,
            'idfinition': self.idfinition,
            'idclient': self.idclient,
            'debuttravaux': self.debuttravaux.isoformat() if self.debuttravaux else None,
            'datedevis': self.datedevis.isoformat() if self.datedevis else None,
            'augmentation': self.augmentation,
            'duree': self.duree,
            'reference':self.reference,
            'lieu':self.lieu
        }

    @classmethod
    def find_by_idClient(cls, num):
        return cls.query.filter_by(idclient=num).all()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        # db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class V_devis(db.Model):
    __tablename__ = 'v_devis'
    __table_args__ = {'info': dict(is_view=True)}

    iddevis = db.Column(db.Integer, primary_key=True) 
    idclient = db.Column(db.String) 
    maison = db.Column(db.String) 
    finition = db.Column(db.String) 
    total = db.Column(db.Float(precision=2)) 
    paye = db.Column(db.Float(precision=2)) 
    reste = db.Column(db.Float(precision=2)) 
    debut = db.Column(db.Date) 
    fin = db.Column(db.Date)
    lieu = db.Column(db.String)
    reference = db.Column(db.String)

    def json(self):
        return {
            'iddevis': self.iddevis,
            'idclient': self.idclient,
            'maison': self.maison,
            'finition': self.finition,
            'total': self.total,
            'paye': self.paye,
            'reste': self.reste,
            'debut': self.debut.strftime('%Y-%m-%d') if self.debut else None,
            'fin': self.fin.strftime('%Y-%m-%d') if self.fin else None,
            'reference':self.reference,
            'lieu':self.lieu,
            'paye-p':100*self.paye/self.total,
            'color':'red' if (100*self.paye/self.total) < 50 else 'green' 
        }

    def getColor(self):
        if (100*self.paye/self.total) > 50:
            return 'green'
        return 'red'