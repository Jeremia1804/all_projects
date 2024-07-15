from objet.LalanaSimba import *
from objet.CoordonneeInfra import *
from base.MyConnection import *
import folium
class Map: 
    
    def __init__(self):
        # Créer une carte centrée sur Madagascar
        lat, lon = [-18.766947, 46.869107]
        self.__m = folium.Map(location=[lat,lon], zoom_start=5)

    def getMap(self):
        map = self.__m
        self.placeLalanaSimba()
        self.placeInfra()
        return map._repr_html_()

    def placeLalanaSimba(self):
        conn = MyConnection.connect()
        coo = LalanaSimba.getAllSimba(conn)
        for co in coo:
            rep1 =LalanaSimba.enleverandsplit(co.getCoo1())
            rep2 =LalanaSimba.enleverandsplit(co.getCoo2())
            coordinates = [
            (float(rep1[0]),float(rep1[1])),(float(rep2[0]),float(rep2[1]))]
            folium.PolyLine(coordinates,tooltip = "RN Simba").add_to(self.__m)
    
    def placeInfra(self):
        conn = MyConnection.connect()
        coo = CoordonneeInfra.getAllInfra(conn)
        for co in coo:
            rep1 =LalanaSimba.enleverandsplit(co.getCoordonnee())
            folium.Marker([float(rep1[0]),float(rep1[1])],popup= co.getNom()).add_to(self.__m)
            # folium.Marker(location=(float(rep1[0]),float(rep1[1])),icon=folium.Icon(color='lightgray',icon='home',prefix='fa')).add_to(self.__m) 

    def save(self):
        self.__m.save('index.html')
