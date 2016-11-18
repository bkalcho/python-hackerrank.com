# Author: Bojan G. Kalicanin
# Date: 18-Nov-2016
#

from collections import namedtuple

n = int(input), Row = namedtuple('Row', input())
a = 0
for i in range(n):
    c = Row(input().split())
    a += int(c.MARKS)
print(a)