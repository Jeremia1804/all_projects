class Fonction:

    def __init__():
        pass

    @staticmethod
    def enlever(point):
        chars = ['P','O','I','N','T','(',')']
        rep = point.translate(str.maketrans({ord(x):'' for x in chars}))
        res = rep.split()
        return res

    @staticmethod
    def getNbInfra(conn,idrn,idinfra,distance,pk1,pk2):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select count(distinct(idcoordonneeInfra)) from (select *,st_distancesphere(ci.cooinfra,pk.coopk) as distance from (select idcoordonneeInfra,idinfra,st_astext(coordonnee) as cooinfra from coordonneeInfra where idinfra="+str(idinfra)+") as ci cross join (select idpk,st_astext(coordonnee) as coopk from pk where valeur>="+str(pk1)+" and valeur<="+str(pk2)+" and idlalana="+str(idrn)+") as pk) h where distance<="+str(distance)

        # print(postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        return row[0][0]

    @staticmethod
    def getNbPopulation(conn,idrn,idinfra,distance,pk1,pk2):
        cursor = conn.cursor()
        postgreSQL_select_Query = "select sum(nombre) from (select distinct(idcoordonneeInfra) as idcoordonneeinfra from (select *,st_distancesphere(ci.cooinfra,pk.coopk) as distance from (select idcoordonneeInfra,idinfra,st_astext(coordonnee) as cooinfra from coordonneeInfra where idinfra="+str(idinfra)+") as ci cross join (select idpk,st_astext(coordonnee) as coopk from pk where valeur>="+str(pk1)+" and valeur<="+str(pk2)+" and idlalana="+str(idrn)+") as pk) h where distance<="+str(distance)+") j join coordonneeInfra on coordonneeInfra.idcoordonneeInfra = j.idcoordonneeInfra"

        # print(postgreSQL_select_Query)
        cursor.execute(postgreSQL_select_Query)
        row = cursor.fetchall()
        if(row[0][0] is None):
            return 0
        return row[0][0]

    @staticmethod 
    def getPosition(conn,lalana1,lalanaH,lalanaP,rayon):
        pos = 0
        for i in range (len(lalanaH)):
            if lalanaH[i].getHopital(conn,rayon)==lalana1.getHopital(conn,rayon):
                pos += i*10
                break
        for i in range (len(lalanaP)):
            if lalanaP[i].getPopulation(conn,rayon)==lalana1.getPopulation(conn,rayon):
                pos += i
                break
        print(lalana1.getIdLalana(),"    ",pos)
        return pos