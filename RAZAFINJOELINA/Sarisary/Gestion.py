from Fonction import *
from Noeud import *
import random
import numpy as np

class Gestion:
    def __init__(self,photo):
        self.photo = photo
        self.noeud = []
        self.largeur = 1
        self.hauteur = 1
        self.diviser(4,3)

    def diviser(self,larg,long):
        self.noeud = []
        sous_images = Fonction.diviserImage(self.photo,larg,long)
        numero = 1
        self.setDimension(larg,long)
        for i in range(len(sous_images)):
            sous = sous_images[i]
            sous_noeud = []
            for j in range (len(sous)):
                sous_noeud.append(Noeud(sous[j],j,i,numero))
                numero  = numero + 1
            self.noeud.append(sous_noeud)

    # def diviser2(self,larg,long):
    #     # self.setDimension(larg,long)
    #     new_noeud = []
    #     for i in range(len(self.noeud)):
    #         sous = self.noeud[i]
    #         new_sous_noeud = []
    #         for j in range (len(sous)):
    #             n = sous[j]
    #             tab = n.getNoeud(larg,long,self.larg,self.hauteur)
    #             for k in range(len(tab)):
    #                 new_sous_noeud.append(tab[k])
    #         new_noeud.append()

    def setDimension(self,larg,hauteur):
        self.largeur = larg
        self.hauteur = hauteur

    def getNoeuds(self):
        tab = []
        for i in range(len(self.noeud)):
            sous = self.noeud[i]
            tab1 = []
            for j in range (len(sous)):
                tab1.append(sous[j].toJson())
            tab.append(tab1)
    
        return tab

    def verification(self):
        for i in range(len(self.noeud)):
            sous = self.noeud[i]
            for j in range (len(sous)):
                print(str(i)+" i = "+str(sous[j].y) + "  et "+ str(j)+" j = "+str(sous[j].x))
                if i!=sous[j].y or j!=sous[j].x:
                    return False
        return True
            

    def manakisaka(self,x1,y1,x2,y2):
        noeud1 = self.noeud[y1][x1]
        noeud2 = self.noeud[y2][x2]
        self.noeud[y1][x1] = noeud2
        self.noeud[y2][x2] = noeud1
        return self.verification()

    def melanger(self):
        for i in range(20):
            x1 = random.randint(0, self.largeur-1)
            x2 = random.randint(0, self.largeur-1)
            y1 = random.randint(0, self.hauteur-1)
            print(x1)
            y2 = random.randint(0, self.hauteur-1)
            self.manakisaka(x1,y1,x2,y2)

    def manodina(self,deg):
        rep=np.array(self.noeud)
        
        if(deg>0):
            self.noeud = np.rot90(rep, k=-1)
        elif(deg<0):
            self.noeud = np.rot90(rep, k=1)

        

    #def rotate90(matrix):
     #   return np.rot90(matrix, k=-1)

    #def rotate_minus_90(matrix):
     #   return np.rot90(matrix, k=1)   

