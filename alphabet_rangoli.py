# Author: Bojan G. Kalicanin
# Date: 09-Oct-2016
# You are given an integer, N. Your task is to print an alphabet rangoli
# of size N. (Rangoli is a form of Indian folk art based on creation
# of patterns.)

import string
alpha = string.ascii_lowercase

n = int(input())
l = []
for i in range(n):
    s = "-".join(alpha[i:n])
    l.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
print('\n'.join(l[:0:-1] + l))