import os
from modules.gen_rand_list import *

os.system('cls')

# Criando o input: 

problem_input = gen_rand_list(5, 99)

print(f'\n entradas: {problem_input}\n')

###

problem_output = problem_input[:3]

for i in problem_input:
    minimal = min(problem_output)
    if i > minimal:
        problem_output[minimal] = i

#for i in problem_input:





print(f'\n saída: {problem_output}\n')

###

sorted_list = sorted(problem_input, reverse=True)
answer = sorted_list[:3]

print(f'\n resposta: {answer}\n')


# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'\nTeste 1: {test1}\n')