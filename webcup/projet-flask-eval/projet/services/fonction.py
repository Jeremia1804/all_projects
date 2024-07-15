from datetime import datetime
from projet.db import db

def getDateActuelle():
    date_actuelle = datetime.now().date()
    return date_actuelle


def delete_all_data(*models):
    try:
        for model in models:
            db.session.query(model).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(str(e))

def delete_model(model):
    db.session.query(model).delete()
    db.session.commit()


def arrondi_formater(nombre_decimal):
    nombre_arrondi = round(nombre_decimal, 2)
    nombre_formate_virgule = f"{nombre_arrondi:,.2f}".replace(',', ' ')
    return nombre_formate_virgule