from MyFile import *
from Graphe import *
from base.MyConnection import *

class Final:
    def __init__(self,con) -> None:
        self.file = MyFile(con)
        self.graphe = Graphe(self.file.ip)
        self.ip = None
        self.site = None
    
    def couper(self,ip1,ip2):
        self.file.cutIp(ip1,ip2)
        self.graphe.G = nx.DiGraph()
        self.graphe.dessiner()
        if self.ip != None:
            self.file.initialiser()
            self.file.misAJourPoids()
            ipe = self.file.search(self.ip,self.site)
            self.graphe.actualiserCourtChemin(ipe,self.file.depart)
        self.graphe.afficher()

        # return self.graphe.finaliser()
    
    def trouver(self,ip,site):
        self.file.initialiser()
        self.file.misAJourPoids()
        ipe = self.file.search(ip,site)
        self.ip = ip
        self.site = site
        self.graphe.G = nx.DiGraph()
        self.graphe.dessiner()

        self.graphe.actualiserCourtChemin(ipe,self.file.depart)
        # return self.graphe.finaliser()
        self.graphe.afficher()