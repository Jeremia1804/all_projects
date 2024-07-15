from PIL import Image
import numpy as np
import tkinter as tk
from os import listdir
from os.path import isfile, join
import pandas as pd
from matplotlib import pyplot as plt

def limiter(mymatrice):
    zero_rows = np.all(mymatrice == 1, axis=1)
    mymatrice = np.delete(mymatrice, np.where(zero_rows)[0], axis=0)
    return mymatrice

def decouper(matrice):
    matrice = matrice.transpose()
    taille = len(matrice)
    mesimages = []
    i = 0
    while i<taille:
        condition = np.all(matrice[i] == 1)
        # print(condition)
        if condition:
            pass
        else:
            image = []
            while condition == False and i<taille:
                image.append(matrice[i])
                i += 1
                if i < taille:
                    condition = np.all(matrice[i] == 1)
            image = np.array(image)
            mesimages.append(image.transpose())
        i += 1
    return mesimages


def binarisationImage(img: Image):
    # nouvelleImage = Image.new(img.mode, img.size)
    nouvelleImage = img.convert('L')
    largeur, hauteur =  img.size
    p=0
    for x in range(largeur):
        for y in range(hauteur):
            pixel = nouvelleImage.getpixel((x,y))
            gris = pixel
            if(isinstance(pixel,int)):
                if(gris > 100):
                    p = 255
                else:
                    p = 0
            elif(isinstance(pixel,tuple)):
                gris = int(0.2125*pixel[0]+0.7154*pixel[1]+0.0721*pixel[2])
                if(gris > 100):
                    p = 255
                else:
                    p = 0

            nouvelleImage.putpixel((x,y), p)
    return nouvelleImage


def generer(size):
    tab = []
    for i in range (size):
        tab.append(1)
    return tab


def carre(matrice):
    larg = len(matrice[0])
    haut = len(matrice)
    i = 0
    if larg < haut:
        ta = haut - larg
        tab = generer(haut)
        while i < ta:
            matrice = np.insert(matrice,-1*(i%2),tab,axis = 1)
            i +=1

    elif larg > haut:
        ta = larg - haut
        tab = generer(larg)
        while i < ta:
            matrice = np.insert(matrice,-1*(i%2),tab,axis = 0)
            i +=1
    return matrice


def centrer(matrice):
        taille = len(matrice)
        tab = generer(taille)
        j = int(taille/5) * 2
        i= 0
        while i < j:
                matrice = np.insert(matrice,-1*(i%2),tab,axis = 0)
                i +=1
        i = 0
        tab = generer(len(matrice))
        while i < j:
                matrice = np.insert(matrice,-1*(i%2),tab,axis = 1)
                i +=1
        return matrice

def configurer(matrice):
    mat = carre(matrice)
    return centrer(mat)

def decoupage(path):
    img = Image.open(path)
    img2 = binarisationImage(img)
    newMatrice = np.array(img2)
    newMatrice = np.where(newMatrice<250,newMatrice,1)
    newMatrice = np.where(newMatrice==1,newMatrice,255)
    # newMatrice =  binaricoder(newMatrice)
    mymatrice = newMatrice
    mymatrice = limiter(mymatrice)
    toi = decouper(mymatrice)
    for i in range (len(toi)):
        toi[i] = configurer(toi[i])
        img = Image.fromarray(toi[i])
        img = img.resize((28,28))
        toi[i] = np.array(img)
        toi[i] = np.where(toi[i]<=1, toi[i],0)
    return toi