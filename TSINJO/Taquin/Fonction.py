import numpy as np
import math
import random

class Fonction:

    @staticmethod
    def trouverelement(matrice,element):
        for i in range(0,matrice.__len__()):
            for j in range (0,matrice[i].__len__()):
                if(matrice[i][j] == element):
                    return [i,j]

    @staticmethod
    def analyse(matrice,element,indices):
        ligne = indices[0]
        col = indices[1]
        fin = matrice.__len__()-1
        lesetat = []
        if(ligne!=0 and ligne!=fin and col!=0 and col!=fin ):
            lesetat = [1,-1,2,-2]
        elif(ligne == 0 and col == 0):
            lesetat = [-1,2]
        elif(ligne == 0 and col == fin):
            lesetat = [-1,-2]
        elif(ligne == fin and col == 0):
            lesetat = [1,2]
        elif(ligne == fin and col == fin):
            lesetat = [1,-2]

        elif(ligne == 0 and col > 0 and col < fin):
            lesetat = [-1,2,-2]
        elif(ligne == fin and col > 0 and col < fin):
            lesetat = [1,2,-2]
        elif(col == 0 and ligne > 0 and ligne<fin):
            lesetat = [-1,1,2]
        elif(col == fin and ligne > 0 and ligne<fin):
            lesetat = [-1,1,-2]

        while element in lesetat:
            lesetat.remove(element)
        return lesetat
    
    @staticmethod
    def bouger(matrice,etat,position):
        newMatrice = np.array(matrice)
        ligne = position[0]
        col = position[1]
        indice = math.fabs(etat)
        if(indice == 2):
            maniere = int(etat/2)
            abouger = newMatrice[ligne][col+maniere]
            newMatrice[ligne][col+maniere] = 0
            newMatrice[ligne][col] = abouger
        elif(indice == 1):
            abouger = newMatrice[ligne-etat][col]
            newMatrice[ligne-etat][col] = 0
            newMatrice[ligne][col] = abouger
        return newMatrice
    
    @staticmethod
    def bouger1(matrice,etat,position):
        newMatrice = matrice
        ligne = position[0]
        col = position[1]
        indice = math.fabs(etat)
        if(indice == 2):
            maniere = int(etat/2)
            abouger = newMatrice[ligne][col+maniere]
            newMatrice[ligne][col+maniere] = 0
            newMatrice[ligne][col] = abouger
        elif(indice == 1):
            abouger = newMatrice[ligne-etat][col]
            newMatrice[ligne-etat][col] = 0
            newMatrice[ligne][col] = abouger

    @staticmethod
    def verifie(tabMatrice, matrice):
        for mat in tabMatrice:
            val = np.array_equiv(mat,matrice)
            if(val == True):
                return 0
        return 1
    
    @staticmethod
    def calcul_heristic(matrice):
        h = 0
        taille = len(matrice)
        for i in range(0,matrice.__len__()):
            for j in range(0,matrice[i].__len__()):
                value = matrice[i][j]
                if(value!=0):
                    target_row = (value-1) // taille
                    target_col = (value -1) % taille
                    h += (math.fabs(i-target_row) + math.fabs(j-target_col))
        return h
    
    @staticmethod
    def inserer(queue,noeud):
        if len(queue) == 0:
            queue.append(noeud)
        else:
            index= 0
            while index<len(queue) and noeud.estimation > queue[index].estimation:
                index += 1
            queue.insert(index,noeud)


    @staticmethod
    def genereSolution(n):
        matrice = [[j+1+n*i for j in range(n)] for i in range(n)]
        matrice[n-1][n-1] = 0
        return np.array(matrice)

    @staticmethod
    def bougerAuHasard(matrice,nombre):
        nouveau = np.array(matrice)
        etat = 0
        position = Fonction.trouverelement(nouveau,0)
        tab = Fonction.analyse(matrice,etat,position)
        i = 0
        while i<nombre:
            index = random.randint(0,len(tab)-1)
            Fonction.bouger1(nouveau,tab[index],position)
            position = Fonction.trouverelement(nouveau,0)
            etat = tab[index]
            tab = Fonction.analyse(matrice,etat,position)
            i +=1
        return nouveau