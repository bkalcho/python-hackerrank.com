# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# If you have N as an input, print on the output 123...N, without
# using string methods

n = int(input())
string = ''
for i in range(1, n + 1):
    string += str(i)

print(string)