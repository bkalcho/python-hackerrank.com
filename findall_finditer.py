# Author: Bojan G. Kalicanin
# Date: 05-Dec-2016
# You are given a string S. It consists of alphanumeric characters,
# spaces and symbols (+,-). Your task is to find all the substrings of S
# that contains 2 or more vowels. Also, these substrings must lie in
# between 2 consonants and should contain vowels only.

import re

s = input()
vowels = 'aeiou'
consonants = 'qwertypsdfghjklzxcvbnm'
re.findall(r'(?<={0:s})({1:s}{2,}){0:s}'.format(consonants, vowels, consonants), s)
print('\n'.join(m or ['-1']))