from objet.Lalana import *
from base.MyConnection import *
from affichage.Map import *
from Affichage import *
from objet.LalanaSimba import *
class Main:
    def executer():
        conn = MyConnection.connect()
        # print(Affichage.afficherLalasimbaParCout())
        # rep = LalanaSimba.getLalanaSimbaById(conn,1)
        # trier = LalanaSimba.getPriority(conn,rep,5000)
        # for i in trier:
        #     print(i.getIdLalanaSimba()," et ",i.getPopulation(conn,5000))
        # op = LalanaSimba.getLalanaPripority(conn,rep,6000)
        # print(op.getIdLalanaSimba())
        # for i in range (len(rep)):
        # priority=LalanaSimba.getLalanaPriporityInfra(conn,1,1)
        # inf=rep[6].getInfraAkaiky(conn,3,6000)
        # la = Lalana.getLalanaById(conn,1)
        # for i in range (len(la.getLalana())):
        #     la.getLalana()[i].calculCout(conn)
        # print(la.calculCoutP())
        # print(Affichage.afficherLalasimbaParCout())
        # for i in priority:                                                                                                           
        #     print(i.getNiveau(),"    ")
        # conn.close()
        ou = Map()
        ou.placeLalanaSimba(conn)
        ou.placeInfra(conn)
        ou.save()
        # lalana = Lalana.getAllLalana(conn)
        # trier = Lalana.getPriority(conn,lalana,5000)
        # for i in trier:
        #     print(i.getNomLalana())
        conn.close()

    executer()

