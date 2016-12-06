# Author: Bojan G. Kalicanin
# Date: 05-Dec-2016
# You are given a string N.
# Your task is to verify that N is a floating point number.

import re

t = int(input())
for i in range(t):
    print(bool(re.search(r'^[+|-]?\d*\.{1}\d+$', input())))