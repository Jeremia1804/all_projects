class Pk:
    __idPk:int
    __coordonnee:str
    __valeur:int
    
    def __init__(self,pk,coo,val):
        self.__idPk = pk
        self.__coordonnee = coo
        self.__valeur = val

    def getIdPk(self):
        return self.__idPk
    def getCoordonnee(self):
        return self.__coordonnee
    def getValeur(self):
        return self.__valeur

    def setIdPk(self,pk):
        self.__idPk = pk
    def setCoordonnee(self,c):
        self.__coordonnee = c
    def setValeur(self,val):
        self.__valeur = val
