# Pangram is a sentence containing every letter in the English alphabet. 
# Given a string, find all characters that are missing from the string, i.e., 
# the characters that can make the string a Pangram. 
# We need to print output in alphabetic order.

problem_input = 'The quick brown fox jumps'

caractere_list = [str for str in problem_input]

caractere_list = list(set(caractere_list))

print(caractere_list)


# problem_output = 