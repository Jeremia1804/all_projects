class Cout:
    __id: int
    __prix:float
    __duree:float
    
    def __init__(self,id,price,dure):
        self.__prix = price
        self.__duree = dure
        self.__id = id

    @staticmethod
    def getCout(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select idcout,prix,duree from cout join (select max(daty) as max from cout) a on cout.daty = a.max"
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        return Cout(row[0][0],row[0][1],row[0][2])

    def getPrix(self):
        return self.__prix
    def getDuree(self):
        return self.__duree

    def setPrix(self,price):
        self.__prix = price
    def setDuree(self, dure):
        self.__duree = dure