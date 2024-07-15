from Fonction import *
import datetime
import calendar
from Cryptography import *

class Mail:
    def __init__(self,id:int,ob,text,compteDestinateur,compteDestinataire,date,etat:int,spam,nomdestinateur,nomdestinataire) -> None:
        self.idMail = id
        self.objet = ob
        self.texte = text
        self.compteDestinateur = compteDestinateur
        self.compteDestinataire = compteDestinataire
        self.nomDestinateur = nomdestinateur
        self.nomDestinataire = nomdestinataire
        self.date = date
        self.spam = spam
        self.etat = etat
    
    def decoder(self,crypt):
        if self.idMail >= 111:
            self.texte = bytes.fromhex(self.texte)
            self.texte = crypt.decrypt_AES(self.texte)
            self.texte = self.texte.decode('utf-8')
        pass

    @staticmethod
    def insererMail(conn,ob,text,id:int,compteDestinataire,spam):
        idMail = insertmail(conn,ob,text)
        insertIsSpam(conn,idMail,spam)
        insertIsRead(conn,idMail,0)
        insertEnvoiMessage(conn,id,compteDestinataire,idMail)
        conn.commit()
    
    @staticmethod
    def repondre(conn,ob,text,id:int,compteDestinataire,idmere,spam):
        idMail = insertmail(conn,ob,text)
        insertResponse(conn,idMail,idmere)
        insertIsSpam(conn,idMail,spam)
        insertIsRead(conn,idMail,0)
        insertEnvoiMessage(conn,id,compteDestinataire,idMail)
        conn.commit()
    
    def getDate(self):
        # Convertir la chaîne en objet de type 'datetime.datetime'.
        date_time_object = datetime.datetime.strptime(str(self.date), "%Y-%m-%d %H:%M:%S.%f")
        jour = date_time_object.day
        mois = date_time_object.month
        annee = date_time_object.year
        heure = date_time_object.hour
        minutes = date_time_object.minute
        nom_mois = calendar.month_name[mois]
        date_en_lettres = f"{jour} {nom_mois} {annee} in {heure:02d}:{minutes:02d}"
        return date_en_lettres
    
    def setSpam(self,etat):
        self.etat = etat