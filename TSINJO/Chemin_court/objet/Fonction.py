from collections import deque

class Fonction:

    @staticmethod
    def inserer(queue,noeud):
        if Fonction.verification(noeud) == 1:
            if len(queue) == 0:
                noeud.done = True
                queue.append(noeud)
            else:
                index= 0
                while index<len(queue) and noeud.poids > queue[index].poids:
                    index += 1
                queue.insert(index,noeud)
    
    @staticmethod
    def verification(noeud):
        if noeud.done == False:
            noeud.done = True
            return 1
        else:
            return 0

    @staticmethod
    def verificationSite(ip,site):
        for si in ip.site:
            if si == site:
                return 1
        return 0
    
    @staticmethod
    def prendre(queue):
        return queue[0]