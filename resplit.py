# Author: Bojan G. Kalicanin
# Date: 05-Dec-2016
# You are given a string S, containing , and/or . and 0-9 digits.
# Your task is to re.split() all of the , and . symbols.

import re

s = input()
a = re.split(r'[,\.]', s)
for i in a:
    if i:
        print(i)