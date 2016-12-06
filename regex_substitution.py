# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given a text of N lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following: && -> and
# || -> or
# Both && and || should have space " " on both sides.

import re

n = int(input())
lines = []
for i in range(n):
    lines.append(input())
text = '\n'.join(lines)
text = re.sub("(?<=\s)\&\&\s", "and ", text)
print(re.sub("\s\|\|\s", " or ", text))