# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Compute cartesian product of two lists.

from itertools import product

a, b = list(map(int, input().split())), list(map(int, input().split()))
s = list((product(a, b)))
n = len(s)
[print(s[i], sep='', end=' ') for i in range(n)]
print()