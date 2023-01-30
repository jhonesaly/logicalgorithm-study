# Algoritmo:

# 1 Sort the array in ascending order.
# 2 Set the low index to the first element of the array and the high index to the last element.
# 3 Set the middle index to the average of the low and high indices.
# 4 If the element at the middle index is the target element, return the middle index.
# 5 If the target element is less than the element at the middle index, set the high index to the middle index – 1.
# 6 If the target element is greater than the element at the middle index, set the low index to the middle index + 1.
# 7 Repeat steps 3-6 until the element is found or it is clear that the element is not present in the array.

import os
import random

# criando variáveis estáticas

list = []
list_range = 10
lim_inf = 0
lim_sup = 99
list_size = 100

# Criando "array" de dados

# for i in range(listrange):
#     num = random.randint(lim_inf, lim_sup)
#     list.append(num)

list = random.sample(range(list_size), list_range)
list.sort()

# Iniciando programa

os.system('cls')

while exit != True:

    outputx = -1 

    # Entrada de dados:

    inputx = input('Digite "exit" para sair ou o número a ser buscado: ')

    # Tratamento dos dados:

    if inputx.isnumeric():
        try:
            inputx = int(inputx)
        except:
            os.system('cls')
            print('digite um número inteiro')

    elif inputx == 'exit':
        os.system('cls')
        print('até a próxima!')
        exit = True
        break

    # Operação dos dados:

    for num in list:
        
        if num == inputx:
            os.system('cls')
            outputx = list.index(inputx)          

    # Saída dos dados: 

    if outputx != -1:
        os.system('cls')
        print(f'o número faz parte da lista! Sua posição na memória é {outputx}')
    
    else:
        os.system('cls')
        print('o número não faz parte da lista!')
