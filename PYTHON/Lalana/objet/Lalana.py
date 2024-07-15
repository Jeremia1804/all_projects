from objet.LalanaSimba import LalanaSimba
from Fonction import Fonction
from objet.Infra import *

class Lalana:
    __idLalana:int
    __nomLalana:str
    __distance:float

    def __init__(self,ide,nom,dist,lar,types):
        self.__idLalana=ide
        self.__nomLalana = nom
        self.__distance = dist
        self.__largeur = lar
        self.__type = types

    @staticmethod
    def getAllLalana(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from lalana"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        l = []
        for row in mobile_records:
            l.append(Lalana(row[0],row[1],row[2],row[3],row[4]))
        return l

    @staticmethod
    def getLalanaById(conn,ide):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from lalana where idLalana = '"+str(ide)+"'"
        # print(postgreSQL_select_Query )
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        for i in range(5):
            lala = Lalana(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        # print(lala.__idLalana)
        return lala
        
    def getCoutRN(self,conn):
        lls = LalanaSimba.getLalanaSimbaById(conn, self.__idLalana)
        cout = 0
        for i in range (len(lls)):
            lls[i].calculCout(conn,self.__largeur)
            cout = cout + lls[i].getCoutP()
            # print(cout,"ar")
        return cout

    @staticmethod
    def convertTime(duree):
        time = []
        if(duree>=24):
            jour = duree//24 # jour
            reste = duree % 24 # heure
        time.append(jour)
        time.append(reste)
        return time

    def getDureeRN(self,conn):
        lls = LalanaSimba.getLalanaSimbaById(conn, self.__idLalana)
        duree = 0
        for i in range (len(lls)):
            lls[i].calculCout(conn,self.__largeur)
            duree = duree + lls[i].getCoutD()
        return duree

    def getHopital(self,conn,rayon):
        idrn = self.getIdLalana()
        idinfra = 2
        pk1 = 0
        pk2 = self.getDistance()
        nb = Fonction.getNbInfra(conn,idrn,idinfra,rayon,pk1,pk2)
        # print(nb,"hop")
        return nb

    def getPopulation(self,conn,rayon):
        idrn = self.getIdLalana()
        idinfra = 3
        pk1 = 0
        pk2 = self.getDistance()
        nb = Fonction.getNbPopulation(conn,idrn,idinfra,rayon,pk1,pk2)
        # print(nb,"pop")
        return nb

    @staticmethod
    def trierHopital(conn,lalana,rayon):
        for i in range (len(lalana)-1):
            k = i + 1
            cle = lalana[k]
            while cle.getHopital(conn,rayon)>lalana[k-1].getHopital(conn,rayon) and k>0:
                lalana[k] = lalana[k-1]
                k -=1
            lalana[k] = cle
        return lalana

    @staticmethod
    def trierPopulation(conn,lalana,rayon):
        for i in range (len(lalana)-1):
            k = i + 1
            cle = lalana[k]
            while cle.getPopulation(conn,rayon)>lalana[k-1].getPopulation(conn,rayon) and k>0:
                lalana[k] = lalana[k-1]
                k -=1
            lalana[k] = cle
        return lalana

    @staticmethod
    def getPriority(conn,lalana,rayon):
        # lalana = Lalana.getAllLalana(conn)
        lalanaH = Lalana.trierHopital(conn,lalana,rayon)
        lalanaP = Lalana.trierPopulation(conn,lalana,rayon)
        lalan = []
        for i in lalana:
            tab = (Fonction.getPosition(conn,i,lalanaH,lalanaP,rayon),i)
            lalan.append(tab)
        lalan.sort(key=lambda x: (-x[0]), reverse=True)
        lalana = []
        for i in lalan:
            lalana.append(i[1])
        return lalana



        
                


    def getIdLalana(self):
        return self.__idLalana
    # def getLalana(self):
    #     return self.__lalana
    def getNomLalana(self):
        return self.__nomLalana
    def getDistance(self):
        return self.__distance
    def getLargeur(self):
        return self.__largeur
    def getType(self):
        return self.__type

    def setIdLalana(self,ide:int):
        self.__idLalana = ide
    # def setLalana(self,ide:int):
    #     self.__lalana = ide
    def setNomLalana(self,nom:str):
        self.__nomLalana = nom
    def setDistance(self,dist:float):
        self.__distance = dist
