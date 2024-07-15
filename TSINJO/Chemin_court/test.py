import networkx as nx
import matplotlib.pyplot as plt
from base.MyConnection import * 
from MyFile import *


conn = MyConnection.connect()
file = MyFile(conn)
# file.couperLienIp(file.ip[0],file.ip[1])
ipe = file.chercher(file.ip[0],file.site[2])



G = nx.DiGraph()

for i in range(len(file.ip)):
    for j in range (file.ip[i].voisins.__len__()):
        G.add_edges_from([(file.ip[i].valeur + "\n" ,file.ip[i].voisins[j].valeur + "\n",{'weight':file.ip[i].poids_voisin[j]})])

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=100)
nx.draw(G,with_labels=True,pos=pos)

labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
if ipe != None:
    while ipe != file.depart:
        nx.draw_networkx_edges(G, pos, edgelist=[(ipe.pred.valeur+"\n", ipe.valeur+"\n")], edge_color='red', width=2.0)
        ipe = ipe.pred
# plt.savefig('./toi.png')
plt.show()
