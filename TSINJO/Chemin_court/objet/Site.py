class Site:
    
    def __init__(self,id:int,nom,url):
        self.id = id
        self.nom = nom
        self.url = url
        self.ip = []

    @staticmethod
    def getSite(conn):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from site"
        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        l = []
        for row in mobile_records:
            l.append(Site(int(row[0]),row[1],row[2]))
        return l

    @staticmethod
    def getOneSommet(ls, id):
        for i in range(ls.__len__()):
            if ls[i].id == id:
                return ls[i]

    def getMyIp(self,conn,ls):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select * from ipsite where idsite = "+ str(self.id)

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()
        for row in mobile_records:
            self.ip.append(Site.getOneSommet(ls, int(row[1])))