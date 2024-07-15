def parenthese(char:str):
    if char=='(':
        return 1
    elif char==')':
        return -1
    return 0

def verification(str:str):
    nb = 0
    for i in range (str.__len__()):
        char = str.__getitem__(i)
        nb = nb + parenthese(char)
        if(nb==-1): return False
    if nb == 0: return True
    else: return False

def toNPI(expr):
    if verification(expr) == False:
        return False
    operators = {'+':1, '-':1, '*':2, '/':2, '^':3}
    accolade = {'(',')'}
    pile = []
    strNpi = ''
    i = 0
    for char in expr:
        if char in operators:
            while pile and operators.get(pile[-1], 0) >= operators[char]:
                strNpi += pile.pop() + ' '
            pile.append(char)
        elif char == '(':
            pile.append(char)
        elif char == ')':
            while pile and pile[-1] != '(':
                strNpi += pile.pop() + ' '
            pile.pop()
        elif char == ' ':
            pass
        else:
            if i+1<expr.__len__():
                if verif(expr.__getitem__(i+1))==False:
                    strNpi += char + ' '
                else:
                    strNpi += char
            else:
                strNpi += char + ' '
        i = i + 1
    while pile:
        strNpi += pile.pop() + ' '
    return strNpi

def verif(char):
    operators = {'0','1','2','3','4','5','6','7','8','9','x'}
    if char in operators:
        return True
    return False

def evaluation(npi):
    operators = {'+', '-', '*', '/', '^'}
    pile = []
    nb = ''
    e = 0
    for char in npi:
        if char in operators:
            e=0
            traitement(pile,char)
        elif char==' ':
            if e==1:
                pile.append(int(nb))
            nb = ''
        else:
            e=1
            nb = nb + char
    return pile[-1]

def traitement(pile,op):
    nb2 = pile.pop()
    nb1 = pile.pop()
    resultat = calcul(nb1,nb2,op)
    pile.append(resultat)

def evaluations(npi):
    operators = {'+', '-', '*', '/', '^'}
    pile = []
    nb = ''
    e = 0
    for char in npi:
        if char in operators:
            e=0
            traitements(pile,char)
        elif char==' ':
            if e==1:
                pile.append(nb)
            nb = ''
        else:
            e=1
            nb = nb + char
    return pile[-1]

def traitements(pile,op):
    nb2 = pile.pop()
    nb1 = pile.pop()
    resultat = calculer(str(nb1),str(nb2),op)
    pile.append(resultat)

def transform():
    pass



def calcul(nb1,nb2,op):
    if op=='+':
        return nb1 + nb2
    elif op=='-':
        return nb1 - nb2
    elif op=='*':
        return nb1 * nb2
    elif op=='/':
        return nb1 / nb2
    elif op=='^':
        return nb1^nb2
    else:
        return 'error'

def hasX(nb,char):
    if char in nb:
        return True
    return False

def split(chaine):
    eto = chaine.split(' ')
    return eto

def spliter(chaine,char):
    eto = chaine.split(char)
    return eto

def liantsoa(d1,d2,operateur):
    x = 0
    nx = 0
    if (operateur == '*'):
        mul = '0'
        toi = None
        if(d1.__len__() == 1 and hasX(d1[0],'x') == False):
            mul = d1[0]
            toi = d2
        else:
            mul = d2[0]
            toi = d1
        for i in toi:
            if(hasX(i,'x') == True):
                nb = extracter(i)
                x = calcul(int(mul),nb,operateur)
                # print(x)
            else:
                nx = calcul(int(mul),int(i),operateur)
                # print()
    else: 
        for i in range(0,d1.__len__()):
            if(hasX(d1[i],'x') == True):
                nb = extracter(d1[i])
                x = calcul(x,nb,'+')
            else:
                nx = calcul(nx,int(d1[i]),'+')
        for i in range(0,d2.__len__()):        
            if(hasX(d2[i],'x') == True):
                nb = extracter(d2[i])
                x = calcul(x,nb,operateur)
            else:
                nx = calcul(nx,int(d2[i]),operateur)


    if (x!= 0 and nx != 0):
        if (nx>0):
            return str(x)+'x +'+str(nx)
        return str(x)+'x '+str(nx)
    elif (nx == 0):
        return str(x)+'x'
    elif(x == 0):
        return str(nx)
    else:
        return '0'

def extracter(nb):
    c = nb.replace('x','')
    if (c==''):
        return 1
    elif(c=='-'):
        return -1
    return int(c)

def calculer(nb1,nb2,operateur):
    c1 = hasX(nb1,'x')
    c2 = hasX(nb2,'x')
    if(c1 == False and c2 == False):
        return calcul(int(nb1),int(nb2),operateur)
    d1 = split(nb1)
    d2 = split(nb2)
    return liantsoa(d1,d2,operateur)

def terminer(equation):
    nb1 = split(equation)
    if(nb1.__len__() == 1 and hasX(nb1[0],'x') == False):
        return 'pas de solution'
    elif(nb1.__len__() == 1 and hasX(nb1[0],'x') == True):
        return 0
    else:
        if(hasX(nb1[0],'x') == False):
            constante = int(nb1[0])*-1
            coefficient = extracter(nb1[1])
            return constante/coefficient
        else:
            constante = int(nb1[1])*-1
            coefficient = extracter(nb1[0])
            return constante/coefficient


def what(equation):
    operator = {'=','>','<'}
    for i in operator:
        if i in equation:
            return i
    return None

def resoudre(equation,etape):
    operation = what(equation)
    etape.append(equation)
    d = spliter(equation,operation)
    membre1 = d[0]
    membre2 = d[1]

    npi1 = toNPI(membre1)
    npi2 = toNPI(membre2)

    v1 = evaluations(npi1)
    v2 = evaluations(npi2)

    etape.append(v1 + operation + v2)
    membreGauche = calculer(v1,v2,'-')

    etape.append(membreGauche +operation+' 0')
    if (operation != '='):
        condition = split(membreGauche)
        for i in range(condition.__len__()):
            if (hasX(condition[i],'x') ==True):
                nb = extracter(condition[i])
                if nb<0 :
                    if(operation=='>'):
                        operation = '<'
                    else:
                        operation = '>'

    valiny = terminer(membreGauche)
    etape.append('x '+operation+' '+str(valiny))
    return valiny

def toString(tab):
    string = ''
    for i in tab:
        string += (i+';')
    return string
# Exemple d'utilisation
# etape = []
# equation = '(0x - 77x + 3) - 1 * (x-2) < 3 * (3x-1)'
# resoudre(equation,etape)
# for a in etape:
#     print(a)
