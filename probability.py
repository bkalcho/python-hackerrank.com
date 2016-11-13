# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Find the probability that at least one of the K indices selected will
# contain the letter: 'a'.

from itertools import combinations

n = int(input())
l = input().split()
k = int(input())
c = list(combinations(l, k))
f = filter(lambda x: 'a' in x, c)
print("{0:.3}".format(len(list(f))/len(c)))