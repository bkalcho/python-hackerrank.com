# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Print all possible combinations, up to size k, of the string in
# lexicographic sorted order.

from itertools import combinations

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
for i in range(1, k+1):
    c = list(combinations(s, i))
    for j in range(len(c)):
        res = ''
        for l in range(i):
            res += c[j][l]
        print(res)