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

# Define todas as arestas

arest = list(itertools.combinations(vert, 2))

# Define peso das arestas

weight_arest = []
for i in range(len(arest)):
    weight_arest.append(random.randint(0,10))

# Desenha as arestas e os vértices

for orig, dest in arest:
    plt.plot([orig[0], dest[0]], [orig[1], dest[1]], 'k-')

plt.scatter(x, y)

# Mostra informações e gráfico

#print(vert)
#print(arest)
#print(weight_arest)
plt.show()