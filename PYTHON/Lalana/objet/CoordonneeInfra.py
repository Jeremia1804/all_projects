class CoordonneeInfra:
    __idInfra:int   
    __id:int
    __nom:str
    __coo:str
    __nb:int
    __infra:str

    def __init__(self,ide,idel,nom,coo,nb,inn):
        self.__id = ide
        self.__idInfra = idel
        self.__nom = nom
        self.__nb = nb
        self.__coo = coo
        self.__infra = inn
    

    @staticmethod
    def getAllInfra(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select ci.idinfra,ci.idcoordonneeinfra,ci.nom,st_astext(ci.coordonnee) as coordonnee, ci.nombre,i.intitule from coordonneeInfra ci natural join infra i"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        simba = []
        for row in mobile_records:
            simba.append(CoordonneeInfra(row[0],row[1],row[2],row[3],row[4],row[5]))
        return simba

    @staticmethod
    def getAllInfraById(conn,idinfra):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select ci.idinfra,ci.idcoordonneeinfra,ci.nom,st_astext(ci.coordonnee) as coordonnee, ci.nombre,i.intitule from coordonneeInfra ci natural join infra i where ci.idinfra="+str(idinfra)
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        simba = []
        for row in mobile_records:
            simba.append(CoordonneeInfra(row[0],row[1],row[2],row[3],row[4],row[5]))
        return simba

    def getInfra(self):
        return self.__infra

    def getIdTousInfra(self):
        return self.__id
    def getIdInfra(self):
        return self.__idInfra
    def getNom(self):
        return self.__nom
    def getNb(self):
        return self.__nb
    def getCoordonnee(self):
        return self.__coo

    def setIdTousInfra(self,ide):
        self.__id  = ide
    def setIdInfra(self,idel):
        self.__idInfra= idel
    def setNom(self,pk):
        self.__nom = pk
    def setNb(self,pk3):
        self.__nb = pk3
    def setCoordonnee(self,coo):
        self.__coo= coo
    def setInfra(self,inn):
        self.__infra = inn