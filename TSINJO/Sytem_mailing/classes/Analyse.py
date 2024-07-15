from base.Executer import *
from Tfidf import *
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pickle

class Analyse:
    def __init__(self) -> None:
        pass

    def recuperationData(self,conn):
        query = "select texte,valeur from mail join v_isspam on mail.idmail = v_isspam.idmail"
        tab = Executer.query(conn,query)
        return tab
    
    def unitaire(self,data,i):
        tab = []
        for row in data:
            tab.append(row[i])
        return tab

    def renouveller(self,conn):
        data = self.recuperationData(conn)
        mails = self.unitaire(data,0)
        valeur = self.unitaire(data,1)
        data,matrix = getMatrix(mails)
        self.ecrireData(data)
        self.apprentissage(valeur,matrix)

    def apprentissage(self,valeur,matrix):
        X = np.array(matrix)
        y = np.array(valeur)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1,random_state = 1)
        clf = RandomForestClassifier(random_state=0)
        clf = clf.fit(X_train, y_train)
        self.ecrireFichier(clf)
    
    def ecrireFichier(self,clf):
        variable_serializee = pickle.dumps(clf)
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/data.pkl", "wb") as fichier:
            fichier.write(variable_serializee)
    
    def ecrireData(self,clf):
        variable_serializee = pickle.dumps(clf)
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/recent.pkl", "wb") as fichier:
            fichier.write(variable_serializee)
    
    def prediction(self,texte):
        clf  = self.lireFichier()
        data = self.lire()
        all_words = data['all_words']
        idf_scores = data['idf_scores']
        matrix = getMatrixPrediction(texte,all_words,idf_scores)
        valiny =  clf.predict([matrix])
        return valiny[0]
    

    def lireFichier(self):
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/data.pkl", "rb") as fichier:
            contenu_fichier = fichier.read()
        return pickle.loads(contenu_fichier)

    def lire(self):
        with open("/home/jeremia/TSINJO/Sytem_mailing/classes/recent.pkl", "rb") as fichier:
            contenu_fichier = fichier.read()
        return pickle.loads(contenu_fichier)
        



