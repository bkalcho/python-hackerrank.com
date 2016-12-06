# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given a string S. Your task is to find the indices of the
# start and end of string k in S.

import re

s, k = input(), input()
p = re.compile(k)
m = p.search(s)
if not m:
    print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = p.search(s, m.start() + 1)