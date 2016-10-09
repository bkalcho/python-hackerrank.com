# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# You are given a string and width. Your task is to wrap the string into
# a paragraph of width w.

import textwrap

s = input()
w = int(input())


print(textwrap.fill(s, w))