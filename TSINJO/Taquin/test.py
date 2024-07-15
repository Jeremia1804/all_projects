import networkx as nx
import matplotlib.pyplot as plt

# Création d'un graphe orienté vide
G = nx.DiGraph()

# Ajout des nœuds avec leurs poids
G.add_node(1, weight=0.5)
G.add_node(2, weight=0.8)
G.add_node(3, weight=1.2)
G.add_node(4, weight=0.7)
G.add_node(5, weight=1.0)

# Ajout des arêtes orientées avec les poids
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

# Récupération des poids des nœuds
weights = nx.get_node_attributes(G, 'weight')

# Récupération des poids des arêtes
edge_labels = nx.get_edge_attributes(G, 'weight')

# Dessin du graphe avec les poids des nœuds et des arêtes
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, arrows=True)

# Affichage des poids des nœuds
nx.draw_networkx_labels(G, pos, labels=weights)

# Coloration d'une arête spécifique
nx.draw_networkx_edges(G, pos, edgelist=[(3, 4),(4, 5)], edge_color='red', width=2.0)

# Affichage des poids des arêtes avec les orientations
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3)

plt.show()
