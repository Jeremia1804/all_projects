def tableau(vola,fameriny):
    if fameriny in vola:
        return fameriny
    nbchiffre = 2
    while nbchiffre*1<fameriny:
        i = 1
        while (nbchiffre-1)*i <fameriny:
            a = traitement(nbchiffre,i,vola,fameriny)
            if a != False:
                return a
            i= i+1
        nbchiffre = nbchiffre + 1
    return "tsy mety ee"
    
def verification(vola,tableau):
    for i in tableau:
        if i not in vola:
            return False
    return True

def recursive(fameriny,nb):
    pass

def traitement(nbchiffre,i,vola,fameriny):
    tab = generer(nbchiffre,i)
    valiny = []
    moi = fameriny - (nbchiffre-1)*i
    tab.append(moi)
    a = verification(vola,tab)
    if a == True:
        print("ito ",tab)
        return tab
    # valiny.append(tab)
    # print(valiny)
    nb2 = tab.pop()
    nb1 = tab.pop()
    while verif2(nb1, nb2) == True:
        tab.append(nb1+1)
        tab.append(nb2-1)
        a = verification(vola,tab)
        print(tab)
        if a == True:
            print("ito ",tab)
            return tab
        # tabe = tab
        # print(tabe)
        # valiny.append(tab)
        # print(valiny)
        nb2 = tab.pop()
        nb1 = tab.pop()
    return False

def verif2(nb1, nb2):
    if nb1 > nb2 or nb1==nb2 or nb1+1 == nb2:
        return False
    return True        


def generer(nbchiffre,i):
    tab = []
    for j in range (nbchiffre-1):
        tab.append(i)
    return tab

print(tableau([2,3,5], 7))