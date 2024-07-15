import numpy as np
from Fonction import Fonction as fonc
class Noeud:
    
    def __init__(self,ma,et,pred,coup = 0,estimations = 0):
        self.matrice = ma
        self.etat = et
        self.predecesseur = pred
        self.coup = coup
        self.estimation = self.coup + estimations

    def generer(self):
        voisin = []
        position = fonc.trouverelement(self.matrice,0)
        tab = fonc.analyse(self.matrice,-1*self.etat,position)
        for i in tab:
            mymatrice = fonc.bouger(self.matrice,i,position)
            estim = fonc.calcul_heristic(mymatrice)
            voisin.append(Noeud(mymatrice,i,self,self.coup+1,estim))
        return voisin    

    