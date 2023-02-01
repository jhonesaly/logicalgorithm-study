# Desafio: https://www.geeksforgeeks.org/missing-characters-make-string-pangram/
# Pangram is a sentence containing every letter in the English alphabet. 
# Given a string, find all characters that are missing from the string, i.e., 
# the characters that can make the string a Pangram. 
# We need to print output in alphabetic order.

import string


problem_input = 'The quick brown fox jumps'

char_list = problem_input.lower()
char_list = [str for str in char_list]
char_list = set(char_list)

char_all = set(string.ascii_letters)

# print(char_all)
# print(char_list)

char_missing = char_all.difference(char_list)
print(char_missing)


# problem_output = qweqweqwe