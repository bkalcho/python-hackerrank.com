# Author: Bojan G. Kalicanin
# Date: 09-Oct-2016
# You are given a string S. Your task is to capitalize each word of S.

s = input()
line = s.split(' ')
print(' '.join((word.capitalize() for word in line)))