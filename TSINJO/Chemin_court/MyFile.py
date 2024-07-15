from collections import deque
from objet.Sommet import *
from objet.Site import *
from objet.Fonction import *

class MyFile:
    def __init__(self,con):
        self.initialiser()
        self.preparation(con)
        # self.couperLienIp(self.ip[0],self.ip[2])
        # self.DeleteSiteInIp(self.ip[1],self.site[1])
    
    def search(self,idip, idsite):
        ip = None
        site = None
        for i in self.ip:
            if(idip == i.id):
                ip = i
                break
        for j in self.site:
            if(idsite == j.id):
                site = j
                break
        return self.chercher(ip,site)
        
    def initialiser(self):
        self.file = deque()
        self.depart = None

    def chercher(self,ip,site):
        self.depart = ip
        self.initialisation(ip)
        if Fonction.verificationSite(ip,site) == 1:
            return ip
        Fonction.inserer(self.file,ip)
        while len(self.file) != 0:
            noeudtraiter = self.file.popleft()
            if Fonction.verificationSite(noeudtraiter,site) == 1:
                return noeudtraiter
            self.misAJourNoeudVoisin(noeudtraiter)
        return None

    def chercher1(self,ip,site):
        e = []
        f = []
        self.depart = ip
        self.initialisation(ip)
        for j in self.allip:
            f.append(j)
        while len(f)!=0:
            noeudtraiter = Fonction.prendre(f)
            self.misAJourNoeudVoisin1(noeudtraiter)
            e.append(noeudtraiter)


    def initialisation(self,ip):
        ip.poids = 0

    def misAJourNoeudVoisin1(self,noeud):
        for i in range(len(noeud.voisins)):
            if(noeud.poids + noeud.poids_voisin[i] < noeud.voisins[i].poids):
                noeud.voisins[i].poids = noeud.poids + noeud.poids_voisin[i]
                noeud.voisins[i].pred = noeud

    def misAJourNoeudVoisin(self,noeud):
        for i in range(len(noeud.voisins)):
            if(noeud.poids + noeud.poids_voisin[i] < noeud.voisins[i].poids):
                noeud.voisins[i].poids = noeud.poids + noeud.poids_voisin[i]
                noeud.voisins[i].pred = noeud
            Fonction.inserer(self.file,noeud.voisins[i])
            
    
    def preparation(self,con):
        self.ip = self.allip(con)
        self.site = self.allsite(con)
        self.getVoisinIp(con)
        self.getSiteIp(con)
        self.getIpSite(con)
        self.definirPoid(con)
    
    def misAJourPoids(self):
        for ip in self.ip:
            ip.poids = math.inf
            ip.done = False
            ip.pred = None
    
    def cutIp(self,id1,id2):
        ip1 = None
        ip2 = None
        for i in self.ip:
            if(id1 == i.id):
                ip1 = i
            elif(id2 == i.id):
                ip2 = i
        self.couperLienIp(ip1,ip2)

    def couperLienIp(self,ip1,ip2):
        a = None
        i = 0
        for ip in ip1.voisins:
            if ip == ip2:
                a = i
                break
            else:
                i += 1
        if a != None:
            del ip1.voisins[a]
            del ip1.poids_voisin[a]

    def DeleteSiteInIp(self,ip1,site):
        a = None
        i = 0
        for si in ip1.site:
            if si == site:
                a = i
                break
            else:
                i += 1
        if a != None:
            del ip1.site[a]
            a = None
            i = 0
            for ip in site.ip:
                if ip == ip1:
                    a = i
                    break
                else:
                    i += 1
            del site.ip[a]


    def allip(self,con):
        return Sommet.getAllSommet(con)

    def allsite(self,con):
        return Site.getSite(con)

    def getVoisinIp(self,con):
        for i in range(len(self.ip)):
            self.ip[i].getVoisin(con,self.ip)
    
    def getSiteIp(self,con):
        for i in range(len(self.ip)):
            self.ip[i].getMySite(con,self.site)

    def getIpSite(self,con):
        for i in range(len(self.site)):
            self.site[i].getMyIp(con,self.ip)
    
    def definirPoid(self,con):
        for i in range(len(self.ip)):
            self.ip[i].getPoids(con)