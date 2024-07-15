from objet.CoordonneeInfra import *
from objet.Cout import *
from base.MyConnection import *
from objet.Lalana import *

class LalanaSimba:
    idLalanaSimba:int
    idLalana:int
    pk1:str
    pk2:str
    niveau:float

    def __init__(self,ide,idel,niv,coo,p1,coo1,p2):
        self.__idLalanaSimba = ide
        self.__idLalana = idel
        self.__pk1 = p1
        self.__pk2 = p2
        self.__niveau = niv
        self.__coo1 = coo
        self.__coo2 = coo1
        self.__coutD = 0
        self.__coutP = 0


    @staticmethod
    def getAllSimba(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from details_simba"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        simba = []
        for row in mobile_records:
            simba.append(LalanaSimba(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        return simba

    @staticmethod
    def getLalanaSimbaById(conn,ide):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from details_simba where idLalana = '"+str(ide)+"'"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        simba = []
        for row in mobile_records:
            simba.append(LalanaSimba(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        return simba

    @staticmethod
    def getOneLalanaSimba(conn,ide,idls):
        l = LalanaSimba.getLalanaSimbaById(conn,ide)
        for i in range(len(l)):
            if (l[i].getIdLalanaSimba()==idls):
                return l[i]
        return 3

    # getidlalanasimbabypriority infra
    @staticmethod
    def getIdPriorite(conn, idinfra):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from priorite where idinfra= '"+str(idinfra)+ "' order by distance"
        
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        idsimba = []
        for row in mobile_records:
            idsimba.append(row[1])
        return idsimba 

    # lalana priorite par infra
    @staticmethod
    def getLalanaPriporityInfra(conn,idl,idinfra):
        id = LalanaSimba.getIdPriorite(conn,idinfra)
        rep = []
        for i in range(len(id)):
            # print(id[i])
            lalana = LalanaSimba.getOneLalanaSimba(conn,idl,id[i])
            # print(lalana)
            rep.append(lalana)
        return rep

    @staticmethod
    def enleverandsplit(point):
        chars = ['P','O','I','N','T','(',')']
        rep = point.translate(str.maketrans({ord(x):'' for x in chars}))
        res = rep.split()
        return res

    def enlever(point):
        chars = ['P','O','I','N','T','(',')']
        rep = point.translate(str.maketrans({ord(x):'' for x in chars}))
        return rep

    def calculCout(self,conn):
        total=0
        longueur = abs(self.__pk2-self.__pk1)*1000
        lala = Lalana.getLalanaById(conn,self.__idLalana)
        # largeur = lala.getLargeur()
        largeur =0
        profondeur = self.__niveau/1000
        couter = Cout.getCout(conn)
        vol = longueur*largeur*profondeur
        self.__coutP = vol*couter.getPrix()
        self.__coutD = vol*couter.getDuree()

    def allInfraAkaikyByType(self,conn,ide,dist):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select co.idcoordonneeinfra from (select co.*,st_distancesphere(st_astext(co.coordonnee),'"+self.__coo1+"') d1,st_distancesphere(st_astext(co.coordonnee),'"+self.__coo2+"') d2 from coordonneeinfra co) co where co.d1<"+str(dist)+" and co.d2<"+str(dist)+" and idinfra="+str(ide)
        print(postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        simba = []
        for row in mobile_records:
            simba.append(row[0])
        return simba

    @staticmethod
    def triParCout(lalana,conn):
        for i in range (len(lalana)):
            lalana[i].calculCout(conn)
        return LalanaSimba.trier(lalana)

    @staticmethod
    def trier(lalana):
        for i in range (len(lalana)-1):
            k = i + 1
            cle = lalana[k]
            while cle.getCoutP()<lalana[k-1].getCoutP() and k>0:
                lalana[k] = lalana[k-1]
                k -=1
            lalana[k] = cle
        return lalana

    def getNbInfraAkaiky(self,conn,ide,dist):
        listid = self.allInfraAkaikyByType(conn,ide,dist)
        infr = []
        for r in listid:
            infr.append(CoordonneeInfra.getAllInfraById(conn,r))
        return infr

    def getInfraAkaiky(self,conn,ide,dist):
        listid = self.allInfraAkaikyByType(conn,ide,dist)
        infr = []
        for r in listid:
            infr.append(CoordonneeInfra.getAllInfraById(conn,r))
        return infr

    def getPopulationAkaiky(self,conn,dist):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select sum(nombre) from (select co.*,st_distancesphere(st_astext(co.coordonnee),'"+self.__coo1+"') d1,st_distancesphere(st_astext(co.coordonnee),'"+self.__coo2+"') d2 from coordonneeinfra co) co where co.d1<"+str(dist)+" and co.d2<"+str(dist)
    
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        return row[0][0]

    @staticmethod
    # priorite par population
    def getLalanaPriporityPopulation(conn,lala,dist):
        pass
        return toreturn

    def getIdLalanaSimba(self):
        return self.__idLalanaSimba
    def getIdLalana(self):
        return self.__idLalana
    def getPk1(self):
        return self.__pk1
    def getPk2(self):
        return self.__pk2
    def getCoo1(self):
        return self.__coo1
    def getCoo2(self):
        return self.__coo2
    def getNiveau(self):
        return self.__niveau
    def getCoutD(self):
        return self.__coutD
    def getCoutP(self):
        return self.__coutP

    def setIdLalanaSimba(self,ide):
        self.__idLalanaSimba  = ide
    def setIdLalana(self,idel):
        self.__idLalana = idel
    def setPk1(self,pk):
        self.__pk1 = pk
    def setPk2(self,pk3):
        self.__pk2 = pk3
    def setCoo1(self,pk):
        self.__coo1 = pk
    def setCoo2(self,pk3):
        self.__coo2 = pk3
    def setNiveau(self,niv):
        self.__niveau = niv