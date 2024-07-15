import json
from flask import Flask, render_template, url_for, request, jsonify
from objet.LalanaSimba import *
from objet.Lalana import *
from base.MyConnection import *
from affichage.Map import *
class Affichage:
    def __init__(self):
        pass
    
    @staticmethod
    def afficherLalasimbaParCout(rayon):
        conn = MyConnection.connect()
        lalana = Lalana.getAllLalana(conn)
        stre = ""
        for la in lalana:
            stre +="<br><table border='1'><tr><td>PK1</td><td>PK2</td><td>Niveau</td><td>Cout par prix</td><td>Cout par Dure</td><td>NB Population</td><td>NB Ecole</td></tr>"
            rep = LalanaSimba.getLalanaSimbaById(conn,la.getIdLalana())
            trier = LalanaSimba.getPriority(conn,rep,rayon)
            # print(len(trier))
            for row in trier:
                row.calculCout(conn,la.getLargeur())
                stre=stre + "<tr><td>"+str(row.getPk1())+"</td><td>"+str(row.getPk2())+"</td><td>"+str(row.getNiveau())+"</td><td>"+str(row.getCoutP())+"</td><td>"+str(row.getCoutD())+"</td><td>"+str(row.getPopulation(conn,rayon))+"</td><td>"+str(row.getHopital(conn,rayon))+"</td></tr>"
            stre+="</table>"
        return stre
    
    @staticmethod
    def afficherLalanaRN(rayon):
        conn = MyConnection.connect()
        lalana = Lalana.getAllLalana(conn)
        trier = Lalana.getPriority(conn,lalana,rayon)
        stre = "<br><table border='1'><tr><td>Route</td><td>Cout</td><td>Duree</td><td>Longueur</td><td>Population</td><td>Ecole</td></tr>"
        for row in trier:
            stre+="<tr><td>"+str(row.getNomLalana())+"</td><td>"+str(row.getCoutRN(conn))+"</td><td>"+str(row.getDureeRN(conn))+"</td><td>"+str(row.getDistance())+"</td><td>"+str(row.getPopulation(conn,rayon))+"</td><td>"+str(row.getHopital(conn,rayon))+"</td></tr>"
        stre+="</table>"
        conn.close()
        return stre