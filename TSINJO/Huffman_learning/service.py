from propriete import language_to_matrix,language_to_matrix2
from sardinas import sardinas
from clf import all_binary_words, ecrireFichier,lireFichier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

def prediction(clf,matrix):
    valiny =  clf.predict([matrix])
    return valiny[0]

def predire(code_str):
    language = code_str.split(',')
    mat_lang = language_to_matrix2(language,all_binary_words)
    clf = lireFichier()
    val = prediction(clf,mat_lang)
    sard = sardinas(language)
    return val,sard

def apprentissage(valeur,matrix):
    X = np.array(matrix)
    y = np.array(valeur)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25,random_state = 1)
    clf = RandomForestClassifier(random_state=0)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    a = accuracy_score(y_test, y_pred)
    print(a)
    return clf

def donneeToMatrix(donnee,all_binary_words = []):
    tab_valeur = []
    tab_matrix = []
    for d in donnee:
        tab_matrix.append(language_to_matrix2(d,all_binary_words))
        tab_valeur.append(sardinas(d))
    return tab_valeur, tab_matrix

def apprendre():
    df = pd.read_csv('data/code.csv')
    df_n = pd.read_csv('data/tsy_code.csv')
    X = df.iloc[:, :].values
    X_n = df_n.iloc[:, :].values
    languages = []
    for d in X:
        languages.append(d[0].split(';'))

    for d in X_n:
        languages.append(d[0].split(';'))
    
    tab_valeur, tab_matrix = donneeToMatrix(languages,all_binary_words)
    clf = apprentissage(tab_valeur,tab_matrix)
    ecrireFichier(clf)