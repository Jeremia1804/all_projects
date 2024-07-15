from base.Executer import *
from Mail import *
from Cryptography import *
class BoiteReception:
    def __init__(self) -> None:
        self.mail = []
        self.crypt = Cryptography()
    
    def getByIdUtilisateur(self,conn,id:int):
        self.mail.clear()
        query = f"select * from mailfinal where iddestinataire = {id} and spam = 'no' order by date_envoi desc"
        tab = Executer.query(conn,query)
        for row in tab:
            mai = Mail(int(row[3]),row[9],row[10],row[5],row[6],row[4],int(row[12]),row[11],row[7],row[8])
            mai.decoder(self.crypt)
            self.mail.append(mai)