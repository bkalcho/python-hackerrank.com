# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# You are given a string S.
# The string contains only lowercase English alphabet characters.
# Your task is to find the top three most common characters in the
# string S.

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass

[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
s = OrderedCounter(sorted(input()))
l = s.most_common(3)
for i in range(3):
    print(l[i][0] + ' ' + str(l[i][1]))