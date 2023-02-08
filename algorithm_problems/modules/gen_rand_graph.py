import numpy as np
import random
import matplotlib.pyplot as plt
import itertools
import os

os.system('cls')

# Define os vértices
x = [1, 2, 2, 3, 4, 4, 5]
y = [2, 1, 3, 2, 1, 3, 2]

vert = []

for i in range(len(x)):
     vert.append((x[i],y[i]))

print(vert)

# Define todas as arestas

arest = list(itertools.combinations(vert, 2))

print(arest)

# Define peso das arestas

weight_arest = []
for i in range(len(arest)):
    weight_arest.append(random.randint(0,10))

print(weight_arest)

# Desenha os vértices

for i in range(len(vert)):
    print(vert[i])
    plt.scatter(vert[i])
plt.show()

# # Desenha as arestas
# for v1, v2 in todas_arestas:
#     plt.plot([x[v1], x[v2]], [y[v1], y[v2]], 'k-')

# # Mostra o gráfico
# plt.show()