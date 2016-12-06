# Author: Bojan G. Kalicanin
# Date: 05-Dec-2016
# You are given a string S. Your task is to find the first occurrence of
# an alphanumeric character in S (read from left to right) that has
# consecutive repetitions.

import re

s = input()
a = re.search(r'([a-zA-Z0-9])\1+', s)
print(a.group(1) if a else -1)