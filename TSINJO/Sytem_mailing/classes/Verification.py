from base.Executer import *
from Utilisateur import *
from Gestion import *

def check(conn,mail,mdp):
        query = f"select * from utilisateur where compte = '{mail}' and mdp = '{mdp}'"
        tab = Executer.query(conn,query)
        if len(tab) == 0:
            return False
        elif len(tab) == 1:
            row = tab[0]
            user = Utilisateur(int(row[0]),row[1],row[2],row[3])
            user.getData(conn)
            gestion = Gestion()
            gestion.setUtilisateur(user)
            return gestion






