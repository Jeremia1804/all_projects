import folium
from generalisation.Base import Base


m = folium.Map()
table=Base.selectWithValeurSelecte(None,"pk","idPk,valeurPk,ST_X(myPoint),ST_Y(myPoint)","")
for i in range(len(table)-1):
    folium.Marker(location=(table[i][2],table[i][3]),icon=folium.Icon(color='lightgray',icon='home',prefix='fa')).add_to(m) 
    #folium.Marker(location=(table[i+1][2],table[i+1][3]),icon=folium.Icon(color='green',icon='home',prefix='fa')).add_to(m) 
m.save("footprint.html")