from objet.LalanaSimba import *
from base.MyConnection import *
from affichage.Map import *
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
        # conn = MyConnection.connect()
        # self.__lalana = LalanaSimba.getLalanaSimbaById(conn,self.__idLalana)
        # conn.close()

    @staticmethod
    def getLalanaById(conn,ide):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from lalana where idLalana = '"+str(ide)+"'"
        print(postgreSQL_select_Query )
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        for i in range(5):
            lala = Lalana(row[0][0],row[0][1],row[0][2],row[0][3],row[0][4])
        print(lala.__idLalana)
        return lala
        
    def getCoutRN(self,conn):
        f = LalanaSimba(1,1,1,1,1,1,1)
        lls = LalanaSimba.getLalanaSimbaById(conn, self.__idLalana)
        cout = 0
        for i in range (len(lls)):
            lls[i].calculCout(conn)
            cout = cout + lls[i].getCoutP()
        return cout


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

