import os
import random

## Criando lista de dados

def gen_rand_list(list_range, lim_sup, lim_inf=0):
    # modo alternativo: list = random.sample(range(list_range), list_size)    
    
    list = []
    for num in range(list_range):
        num = random.randint(lim_inf, lim_sup)
        list.append(num)
    return list

os.system('cls')

# Criando o input: 

problem_input = gen_rand_list(10, 99)

print(f'\n entradas: {problem_input}\n')

###



###

answer = sorted(problem_input)

print(f'\n resposta: {answer}\n')


# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'\nTeste 1: {test1}\n')