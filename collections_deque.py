# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# Perform append, pop, popleft and appendleft methods on an empty deque d.

from collections import deque

n = int(input())
d = deque()
for i in range(n):
    line = input().split()
    if len(line) < 2:
        comm = line[0]
        exec('d.' + comm + '()')
    else:
        comm = line[0]
        el = line[1]
        exec('d.' + comm + '(' + el + ')')
[print(d[i], end=' ') for i in range(len(d))]