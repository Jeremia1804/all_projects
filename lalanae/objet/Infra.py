class Infra:
    __idInfra:int
    __intitule:str

    def __init__(self,ide:int,nom:str):
        self.__idInfra = ide
        self.__intitule = nom

    def getIdInfra(self):
        return self.__idInfra
    def getIntitule(self):
        return self.__intitule
    
    def setIdInfra(self,ide:int):
        self.__idInfra = ide
    def setIntitule(self,nom:str):
        self.__intitule = nom

    