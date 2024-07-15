from base.MyConnection import *
from base.Executer import *
from Utilisateur import *
from Fonction import *
from Mail import *
import pickle
class Gestion:
    def __init__(self) -> None:
        self.conn = MyConnection.connect()
        self.utilisateur = None
        self.nb = 0
        self.lireFichier()

    def setUtilisateur(self,user):
        self.utilisateur = user
    
    def actualiser(self):
        self.utilisateur.getData(self.conn)

    def insertIsSpam(self,idmail,spam):
        insertIsSpam(self.conn,idmail,spam)

    def insertIsRead(self,idmail,etat):
        insertIsRead(self.conn,idmail,etat)

    def envoiMail(self,ob,text,compteDestinataire,spam):
        Mail.insererMail(self.conn,ob,text,self.utilisateur.id,compteDestinataire,spam)

    def repondre(self,mailMere,text,spam):
        compte  = None
        if self.utilisateur.compte == mailMere.compteDestinataire:
            compte = mailMere.compteDestinateur
        else:
            compte = mailMere.compteDestinataire
        Mail.repondre(self.conn,mailMere.objet,text,self.utilisateur.id,compte,mailMere.idMail,spam)

    def clear(self):
        self.utilisateur = None

    def getBoiteReception(self):
        return self.utilisateur.boitereception.mail

    def getEnvoyes(self):
        return self.utilisateur.envoyes.mail
    
    def getSpam(self):
        return self.utilisateur.spam.mail
    
    def getMailById(self,id):
        for mail in self.utilisateur.boitereception.mail:
            if mail.idMail == id:
                return mail
        for mail in self.utilisateur.envoyes.mail:
            if mail.idMail == id:
                return mail
        
        for mail in self.utilisateur.spam.mail:
            if mail.idMail == id:
                return mail
        return None
    
    def verifierMail(self,id):
        for mail in self.utilisateur.boitereception.mail:
            if mail.idMail == id:
                return True
        for mail in self.utilisateur.spam.mail:
            if mail.idMail == id:
                return True
        return False
    
    def lireFichier(self):
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/data.pkl", "rb") as fichier:
            contenu_fichier = fichier.read()
        self.clf = pickle.loads(contenu_fichier)
