from collections import deque
from Noeud import Noeud
from Fonction import Fonction as fonc
import numpy as np

class Final:
    
    def __init__(self,mat):
        self.initialisation(mat)
    
    def preparer(self):
        coup = 0
        self.existing.append(self.resolu)
        estim = fonc.calcul_heristic(self.resolu)
        self.depart = Noeud(self.resolu,0,None,coup,estim)
        self.file.append(self.depart)
        i = 0
        j = 0
        while len(self.file) != 0 and i == 0:
            noeud = self.file.popleft()
            voisin = noeud.generer()
            j +=1
            # print(j)
            for n in voisin:
                if (np.array_equal(n.matrice,self.solution) == True):
                    i = 1
                    return n
                val = fonc.verifie(self.existing,n.matrice)
                print(val)
                if(val == 1):
                    self.existing.append(n.matrice)
                    fonc.reinserer(self.file,n)

    def chemin(self,valiny):
        toReturn = []
        while self.depart != valiny:
            toReturn.insert(0,valiny.etat)
            valiny = valiny.predecesseur
        return toReturn
    


    def initialisation(self,mat):
        self.file = deque()
        self.solution = fonc.genereSolution(4)
        self.depart = None
        self.existing = []
        self.resolu = mat
        # self.resolu = np.array([[5,15,11,10],[4,13,14,9],[7,12,6,2],[1,3,8,0]])
        # self.resolu = fonc.bougerAuHasard(self.solution,50)