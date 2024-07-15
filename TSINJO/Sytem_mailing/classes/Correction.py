import pickle
from base.Executer import *
class Correction:
    def __init__(self) -> None:
        pass
    
    def recuperationData(self,conn):
        query = "select texte,valeur from mail join v_isspam on mail.idmail = v_isspam.idmail"
        tab = Executer.query(conn,query)
        return tab
    
    def unitaire(self,data,i):
        tab = []
        for row in data:
            tab.append(row[i])
        return tab

    def ecrireFichier(self,clf):
        variable_serializee = pickle.dumps(clf)
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/meswords.pkl", "wb") as fichier:
            fichier.write(variable_serializee)

    def lireFichier(self):
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/meswords.pkl", "rb") as fichier:
            contenu_fichier = fichier.read()
        return pickle.loads(contenu_fichier)