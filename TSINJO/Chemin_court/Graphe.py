import networkx as nx
import matplotlib.pyplot as plt

class Graphe:
    def __init__(self,ips):
        self.ip = ips
        self.G = nx.DiGraph()
        self.pos = None

    def dessiner(self):
        for i in range(len(self.ip)):
            for j in range (self.ip[i].voisins.__len__()):
                self.G.add_edges_from([(self.ip[i].valeur + "\n" ,self.ip[i].voisins[j].valeur + "\n",{'weight':self.ip[i].poids_voisin[j]})])

        self.pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G,self.pos,node_size=100)
        nx.draw(self.G,with_labels=True,pos=self.pos)

        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=labels)
        # plt.show()

    def actualiserCourtChemin(self,ipe,depart):
        if ipe != None:
            while ipe != depart:
                nx.draw_networkx_edges(self.G, self.pos, edgelist=[(ipe.pred.valeur+"\n", ipe.valeur+"\n")], edge_color='red', width=2.0)
                ipe = ipe.pred

    def finaliser(self):
        graph_html = nx.nx_agraph.graphviz_layout(self.G, prog = 'dot', root='A')
        return graph_html

    def afficher(self):
        plt.savefig('./static/img/toi.png')
        plt.show()