import numpy as np
import matplotlib.pyplot as plt
import itertools
import networkx as nx

# Define os vértices
x = [1, 2, 2, 3, 4, 4, 5]
y = [2, 1, 3, 2, 1, 3, 2]

v = []

for i in range(len(x)):
     v.append((x[i],y[i]))

print(v)

# Define peso das arestas
todas_arestas = list(itertools.combinations(range(len(x)), 2))

n = 6
matriz_pesos = 10*(np.random.rand(n, n))
n = len(matriz_pesos)
for i in range(n):
    matriz_pesos[i, i] = 0
n = len(matriz_pesos)
for i in range(n-1, -1, -1):
    matriz_pesos[i, i] = 0

print(n)
print(matriz_pesos)

# Desenha os vértices
plt.scatter(x, y)

# Desenha as arestas
for v1, v2 in todas_arestas:
    plt.plot([x[v1], x[v2]], [y[v1], y[v2]], 'k-')

# Mostra o gráfico
plt.show()

# Executa o algoritmo de Prim
G = nx.Graph()
G.add_nodes_from(range(len(x)))

# Adiciona as arestas com seus pesos
for i, (v1, v2) in enumerate(todas_arestas):
    peso = matriz_pesos[v1][v2]
    G.add_edge(v1, v2, weight=peso)

mst = nx.minimum_spanning_tree(G, weight='weight')

# Desenha as arestas da Minimum Spanning Tree com cor vermelha
for u, v in mst.edges:
    plt.plot([x[u], x[v]], [y[u], y[v]], 'r-')

# Mostra o gráfico
plt.show()
