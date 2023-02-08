import networkx as nx
from modules.gen_rand_graph import *


# Executa o algoritmo de Prim
G = nx.Graph()
G.add_nodes_from(range(len(x)))

# Adiciona as arestas com seus pesos
for i, (v1, v2) in enumerate(todas_arestas):
    peso = matriz_pesos[v1][v2]
    G.add_edge(v1, v2, weight=peso)

mst = nx.minimum_spanning_tree(G, weight='weight')

# Desenha as arestas da Minimum Spanning Tree com cor vermelha
for u, vert in mst.edges:
    plt.plot([x[u], x[vert]], [y[u], y[vert]], 'r-')

# Mostra o gráfico
plt.show()
