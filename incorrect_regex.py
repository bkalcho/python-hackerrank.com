# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

import re

for i  in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)