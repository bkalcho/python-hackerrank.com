# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given N lines of CSS code. Your task is to print all valid Hex
# Color Codes, in order of their occurrence from top to bottom.

import re

n = int(input())
pattern = re.compile('#[a-f\d]{6}|#[a-f\d]{3}', re.I)
for i in range(n):
    m = pattern.findall(input()[1:])
    if m:
        print(*m, sep='\n')
    else:
        None