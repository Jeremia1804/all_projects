from objet.Site import *
import math
class Sommet:
    
    def __init__(self,id:int,valeur):
        self.id = id 
        self.valeur = valeur
        self.pred = None
        self.poids = math.inf
        self.site = []
        self.voisins = []
        self.poids_voisin = []
        self.done = False

    @staticmethod
    def getAllSommet(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from ip"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        l = []
        for row in mobile_records:
            l.append(Sommet(int(row[0]),row[1]))
        return l

    @staticmethod
    def getOneSommet(ls, id):
        for i in range(ls.__len__()):
            if ls[i].id == id:
                return ls[i]

    def getVoisin(self,conn,ls):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from lienip where idip1 = "+ str(self.id)

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            self.voisins.append(Sommet.getOneSommet(ls, int(row[2])))
    
    def getMySite(self,conn,ls):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from ipsite where idip = "+ str(self.id)

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            self.site.append(Sommet.getOneSommet(ls, int(row[2])))
    

    def getPoids(self,conn):
        for voisin in self.voisins:
            cursor = conn.cursor()
            postgreSQL_select_Query = "select poids from lienip where idip1 = "+ str(self.id) +" and idip2="+ str(voisin.id)

            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall()
            self.poids_voisin.append(float(mobile_records[0][0]))

