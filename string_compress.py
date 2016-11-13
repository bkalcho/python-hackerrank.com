# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# 

from itertools import groupby

s = list(input())
cum = ''
for key, group in groupby(s, lambda x: x):
    s = 0
    for t in group:
        s += 1
    cum += '('+ str(s) + ', ' + key + ') '
print(cum)