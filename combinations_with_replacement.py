# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Print all possible size k replacement combinations of the string in
# lexicographic sorted order.

from itertools import combinations_with_replacement

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
cr = list(combinations_with_replacement(s, k))
for i in range(len(cr)):
    res = ''
    for j in range(k):
        res += cr[i][j]
    print(res)