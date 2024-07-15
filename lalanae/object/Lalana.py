from base.MyConnection import *
from object.LalanaSimba import *
class Lalana:
    __idLalana:int
    __nomLalana:str
    __distance:float

    def __init__(self,ide,nom,dist,lar):
        self.__idLalana=ide
        self.__nomLalana = nom
        self.__distance = dist
        self.__largeur = lar
        self.__lalana = []
        # conn = MyConnection.connect()
        # self.getLalanaSimba(conn)

    def getLalanaSimba(self,conn):
        self.__lalana = LalanaSimba.getLalanaSimbaById(conn,self.__idLalana)

    @staticmethod
    def getLalanaById(conn,ide):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from lalana where idLalana = '"+str(ide)+"'"
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        
        lala = Lalana(row[0][0],row[0][1],row[0][2],row[0][3])
        return lala


    def getIdLalana(self):
        return self.__idLalana
    def getLalana(self):
        return self.__lalana
    def getNomLalana(self):
        return self.__nomLalana
    def getDistance(self):
        return self.__distance
    def getLargeur(self):
        return self.__largeur

    def setIdLalana(self,ide:int):
        self.__idLalana = ide
    def setLalana(self,ide:int):
        self.__lalana = ide
    def setNomLalana(self,nom:str):
        self.__nomLalana = nom
    def setDistance(self,dist:float):
        self.__distance = dist

