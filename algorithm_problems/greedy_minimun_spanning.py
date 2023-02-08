import networkx as nx
import sys

sys.path.append('modules')
import modules.gen_rand_graph

# # Executa o algoritmo de Prim
# G = nx.Graph()
# G.add_nodes_from(range(len(x)))

# # Adiciona as arestas com seus pesos
# for i, (orig, dest) in enumerate(todas_arestas):
#     peso = matriz_pesos[orig][dest]
#     G.add_edge(orig, dest, weight=peso)

# mst = nx.minimum_spanning_tree(G, weight='weight')

# # Desenha as arestas da Minimum Spanning Tree com cor vermelha
# for u, vert in mst.edges:
#     plt.plot([x[u], x[vert]], [y[u], y[vert]], 'r-')

# # Mostra o gráfico
# plt.show()
