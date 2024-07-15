from base.Executer import *
def insertmail(conn,ob,text):
    query = f"insert into mail values (default,'{ob}','{text}')"
    Executer.insert(conn,query)
    query = "select  idmail from mail order by idmail desc limit 1"
    tab= Executer.query(conn,query)
    return int(tab[0][0])

def insertResponse(conn,idmail,idMere):
    query = f"insert into response values (default,{idmail},{idMere})"
    Executer.insert(conn,query)

def verifyRead(conn,idmail):
    query = f"select  valeur from isread where idmail = {idmail}"
    tab= Executer.query(conn,query)
    if(len(tab)>0):
        return int(tab[0][0])
    return None

def insertIsSpam(conn,idmail,spam):
    query = f"insert into isspam values (default,{idmail},'{spam}')"
    Executer.insert(conn,query)
    conn.commit()

def insertIsRead(conn,idmail,etat):
    nb = verifyRead(conn,idmail)
    if(etat != nb):
        query = f"insert into isread values (default,{idmail},{etat})"
        print(query)
        Executer.insert(conn,query)
        conn.commit()


def insertEnvoiMessage(conn,iddestinateur,comptedestinataire,idmail):
    iddestinataire = getIdUtilisateur(conn,comptedestinataire)
    query = f"insert into envoimessage values (default,{iddestinateur},{iddestinataire},{idmail},now())"
    Executer.insert(conn,query)

def getIdUtilisateur(conn,compte):
    query = f"select  idutilisateur from utilisateur where compte = '{compte}'"
    tab= Executer.query(conn,query)
    return int(tab[0][0])