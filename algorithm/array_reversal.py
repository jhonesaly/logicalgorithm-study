import os
from modules.gen_rand_list import *

os.system('cls')

# Criando o input: 

# problem_input = gen_rand_list(5, 99)

problem_input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
problem_input2 = 3

print(f'\nentradas: {problem_input1} , {problem_input2}\n')


###

problem_output = [range(problem_input2)]

for i in range(problem_input2):
    aux_1 = problem_input1.pop(-1)
    problem_output[len(problem_output)-i] = aux_1

problem_output.append(problem_input1)



print(f'\nsaída: {problem_output}\n')

###

answer = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]

print(f'\nresposta: {answer}\n')


# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'\nTeste 1: {test1}\n')