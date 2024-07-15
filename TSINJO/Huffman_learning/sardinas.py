def calcul_L0(language):
    return set(language)

def calcul_L1(language):
    resid = quotient(language,language)
    resid.remove("")
    return resid


def residuel(mot, language):
    residuel_set = set()
    for word in language:
        if word.startswith(mot):
            residuel_set.add(word[len(mot):])
    return residuel_set

def setMoi(set1, set2):
    for element in set2:
        set1.add(element)

def quotient(language1, language2):
    quotient_set = set()
    for word in language1:
        residual_set = residuel(word, language2)
        setMoi(quotient_set,residual_set)
    return quotient_set

def sardinas(language):
    l0 = calcul_L0(language)
    if(len(l0) == 1):
        return True
    else:
        l1 = calcul_L1(l0)
        tab_set = [l0,l1]
        return ln(tab_set,2)

def ln(tab_set,indice):
    lang_princ = tab_set[0]
    lang_moins = tab_set[indice-1]
    valiny = ln_mitohy(lang_princ,lang_moins)
    tab_set.append(valiny)

    if len(valiny) == 0:
        return True
    elif contient_eps(valiny) == True:
        return False
    elif has_duplicates(tab_set) == True:
        return True
    else:
        return ln(tab_set,indice+1)


def ln_mitohy(lang_principal,lang_moins):
    resid1 = quotient(lang_principal,lang_moins)
    resid2 = quotient(lang_moins,lang_principal)
    setMoi(resid1,resid2)
    return resid1

def contient_eps(set1):
    for item in set1:
        if item == "":
            return True
    return False

def has_duplicates(tab):
    tuple_set = set()
    for s in tab:
        tuple_set.add(tuple(sorted(s)))
    
    if len(tuple_set) < len(tab):
        return True
    else:
        return False
