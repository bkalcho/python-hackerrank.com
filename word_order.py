# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# You are given n words. Some words may repeat. For each word, output
# its number of occurrences. The output order should correspond with the
# input order of appearance of the word. See the sample input/output for
# clarification.

from collections import OrderedDict

n = int(input())
d = OrderedDict()
for i in range(n):
    word = input()
    d[word] = d.get(word, 0) + 1
print(len(d))
for k, v in d.items():
    print(v, end=' ')