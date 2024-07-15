from joblib import *

def predire(matrice,clf):
    aRetourner = clf.predict(matrice)
    return aRetourner

def transformToString(matrices):
    aRetourner = ''
    clf = load('model_signe.joblib')
    for mat in matrices:
        aRetourner += predire(mat,clf)
    return aRetourner