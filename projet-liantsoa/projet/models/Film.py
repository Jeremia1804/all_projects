from projet.db import db

class Film(db.Model):
    __tablename__ = 'film'
    
    id = db.Column(db.Integer, primary_key = True)
    titre = db.Column(db.String(20))
    auteur  = db.Column(db.String(20))
    duree  = db.Column(db.Float)
    
    idcategorie = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    
    def __init__(self, name):
        self.name = name
        
    # def json(self):
    #     return {'name': self.name}
    
    @classmethod
    def find_all(cls):
        return cls.query.all()
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()