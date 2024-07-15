from projet.db import db
from sqlalchemy import text


class MaisonModel(db.Model):
    __tablename__ = 'maison'
    
    idmaison= db.Column(db.Integer, primary_key=True)
    libelle=db.Column(db.String)
    duree=db.Column(db.Float)
    surface = db.Column(db.Float)
    descriptions = db.Column(db.String)
    
    def __init__(self, libelle,duree, surface):
        self.libelle = libelle
        self.duree = duree
        self.surface = surface

    def json(self):
        return {
            'libelle':self.libelle,
            'id':self.idmaison,
            'duree':self.duree,
            'surface':self.surface
        }

    def repareDescription(self):
        data = self.descriptions.split(',')
        self.details = [d for d in data]
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(idmaison=id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()