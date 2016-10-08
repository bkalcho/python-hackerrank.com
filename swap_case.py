# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# You are given a string . Your task is to swap cases. In other words,
# convert all lowercase letters to uppercase letters and vice versa.

line = input()
# Simplest way, using swapcase() method
# print(line.swapcase())
string = ''
for i in range(len(line)):
    if line[i].islower():
         string += line[i].upper()
    else:
        string += line[i].lower()

print(string)