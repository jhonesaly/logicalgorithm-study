# Algoritmo: https://www.geeksforgeeks.org/counting-sort/

# Counting sort is a sorting technique based on keys between a specific range. 
# It works by counting the number of objects having distinct key values (a kind of hashing). 
# Then do some arithmetic operations to calculate the position of each object in the output sequence. 

problem_input = [1, 4, 1, 2, 7, 5, 2]

# Criando chave 

key_index = list(range(min(problem_input),max(problem_input)+1))
key_zeros = list(0 for i in range(len(key_index)))

for i1 in range(len(problem_input)):
    for i2 in range(len(key_index)):
        if key_index[i2] == problem_input[i1]:
            key_zeros[i2] += 1

problem_output = [0 for i in range(len(problem_input))]

for i1 in range (len(problem_output)):
    
    if key_zeros[i1] != 0:
        problem_output[i1] = key_index[i1]
        key_zeros[i1] -= 1

# print(key_index)
print(key_zeros)
print(problem_output)


answer = sorted(problem_input)
# print(answer)

# Teste

test1 = False

if answer == problem_output:
    test1 = True

print(f'Teste 1: {test1}')