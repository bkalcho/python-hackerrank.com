# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Print all possible permutations of the size kof the string in
# lexicographic sorted order.

from itertools import permutations

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
p = list(permutations(s, k))
for i in range(len(p)):
    res = ''
    for j in range(k):
        res += p[i][j]
    print(res)