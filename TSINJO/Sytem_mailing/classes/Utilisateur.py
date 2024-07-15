from BoiteReception import *
from Sent import *
from Spam import *
class Utilisateur:
    def __init__(self,id:int,nom,compte,mdp) -> None:
        self.id = id
        self.nom = nom
        self.compte = compte
        self.mdp = mdp
        self.boitereception = BoiteReception()
        self.envoyes = Sent()
        self.spam = Spam()

    def getData(self,conn):
        self.boitereception.getByIdUtilisateur(conn,self.id)
        self.envoyes.getByIdUtilisateur(conn,self.id)
        self.spam.getByIdUtilisateur(conn,self.id)
    
    def toJson(self):
        info = {
            "nom":self.nom,
            "id":self.id,
            "compte":self.compte,
            "mdp":self.mdp
        }
        return info