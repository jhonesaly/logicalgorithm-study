# Desafio: https://www.geeksforgeeks.org/bubble-sort/
# Bubble Sort is the simplest sorting algorithm that works by repeatedly # swapping the adjacent elements if they 
# are in the wrong order. This algorithm # is not suitable for large data sets as its average and worst-case time 
# complexity is quite high.

import os

os.system('cls')

problem_input = [5, 1, 4, 2, 8]

# Solution 1:

# problem_input.sort()
# print(problem_input)

# Solution 2 (algorithm):

list_raw = problem_input

while ... :
    for i in range(len(list_raw)):
        print(i)
        try:
            if list_raw[i] > list_raw[i+1]:
                num_l = list_raw[i]
                num_r = list_raw[i+1]
                list_raw[i] = num_r
                list_raw[i+1] = num_l
        except:
            break

print(list_raw)

problem_answer = [1, 2, 4, 5, 8] 
