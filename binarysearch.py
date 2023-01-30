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

list_bs = []
list_size = 10
lim_inf = 0
lim_sup = 99
list_range = 100

# Criando funções

def calc_mid_index(lim_inf, lim_sup):
    mid_index = int((lim_inf + lim_sup)/2)
    return mid_index

# def default(list_bs):
#     list_size = len(list_bs)
#     hi_index = list_size-1
#     low_index = 0
#     mid_index = calc_mid_index(low_index, hi_index)
#     num_mid_index = list_bs[mid_index]
#     return hi_index, low_index, mid_index, num_mid_index

# Criando "array" de dados

# for i in range(listrange):
#     num = random.randint(lim_inf, lim_sup)
#     list.append(num)

list_bs = random.sample(range(list_range), list_size)
list_bs.sort()

list_bs = [0, 1, 34, 38, 50, 69, 81, 82, 87, 94]

# Iniciando programa

os.system('cls')

exit = False

while exit != True:

    print(f'a lista é: {list_bs}')
    #default(list_bs)
    
    hi_index = list_size-1
    low_index = 0
    mid_index = calc_mid_index(low_index, hi_index)
    num_mid_index = list_bs[mid_index]

    search = input('Digite o número a ser procurado: ')

    if search == 'exit':
        exit = True
        break

    else:
        search = int(search)
    
    if search >= list_bs[0] and search <= list_bs[list_size-1]:
        
        while low_index != hi_index:
        
            if search == num_mid_index:
                break

            elif search > num_mid_index:
                low_index = mid_index
                mid_index = calc_mid_index(low_index, hi_index)
                num_mid_index = list_bs[mid_index]

            elif search < num_mid_index:
                hi_index = mid_index
                mid_index = calc_mid_index(low_index, hi_index)
                num_mid_index = list_bs[mid_index]

        if search == num_mid_index:
            os.system('cls')
            print('O número está na lista!')
            print(f'O index do número é: {list_bs.index(search)}')
        
        else:
            os.system('cls')
            print('O número procurado não está na lista!')

    else:
        os.system('cls')
        print('O número procurado não está na lista!')

