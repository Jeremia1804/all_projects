from objet.LalanaSimba import *
from objet.CoordonneeInfra import *
from base.MyConnection import *
import folium
class Map: 
    
    def __init__(self):
        # Créer une carte centrée sur Madagascar
        lat, lon = [-18.766947, 46.869107]
        self.__m = folium.Map(location=[lat,lon], zoom_start=5)

    def placeLalanaSimba(self,conn):
        coo = LalanaSimba.getAllSimba(conn)
        for co in coo:
            rep1 =Fonction.enlever(co.getCoo1())
            rep2 =Fonction.enlever(co.getCoo2())
            coordinates = [
            (float(rep1[0]),float(rep1[1])),(float(rep2[0]),float(rep2[1]))]
            folium.PolyLine(coordinates,tooltip = "RN Simba").add_to(self.__m)
    
    def placeInfra(self,conn):
        # coo = CoordonneeInfra.getAllInfra(conn)
        # for co in coo:
        #     rep1 =Fonction.enlever(co.getCoordonnee())
        #     folium.Marker([float(rep1[0]),float(rep1[1])],popup= co.getNom()).add_to(self.__m)
        #     folium.Marker(location=(float(rep1[0]),float(rep1[1])),icon=folium.Icon(color='lightgray',icon='home',prefix='fa')).add_to(self.__m) 
        hop = CoordonneeInfra.getAllInfraById(conn,1)
        ecole = CoordonneeInfra.getAllInfraById(conn,2)
        village = CoordonneeInfra.getAllInfraById(conn,3)

        feature_groupH = folium.FeatureGroup("Hopital")
        feature_groupE = folium.FeatureGroup("Ecole")
        feature_groupM = folium.FeatureGroup("Village")

        print(len(hop),"hopital")
        print(len(village),"village")
        print(len(ecole),"ecole")
        for i in range (len(hop)):
            rep1 =Fonction.enlever(hop[i].getCoordonnee())
            folium.Marker([float(rep1[1]),float(rep1[0])],popup= hop[i].getNom(),icon=folium.Icon(color="purple",icon="hospital",prefix="fa")).add_to(feature_groupH)

        for i in range (len(ecole)):
            rep1 =Fonction.enlever(ecole[i].getCoordonnee())
            folium.Marker([float(rep1[1]),float(rep1[0])],popup= ecole[i].getNom(),icon=folium.Icon(color="black",icon="school",prefix="fa")).add_to(feature_groupE)

        for i in range (len(village)):
            rep1 =Fonction.enlever(village[i].getCoordonnee())
            folium.Marker([float(rep1[1]),float(rep1[0])],popup= village[i].getNb(),icon=folium.Icon(color="beige",icon="user",prefix="fa")).add_to(feature_groupM)
        
        feature_groupH.add_to(self.__m)
        feature_groupE.add_to(self.__m)
        feature_groupM.add_to(self.__m)
        folium.LayerControl().add_to(self.__m)

    def save(self):
        self.__m.save('index.html')
