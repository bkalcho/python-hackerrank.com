# Author: Bojan G. Kalicanin
# Date: 07-Dec-2016
# Neo has a complex matrix script. The matrix script is a NxM grid of
# strings. It consists of alphanumeric characters, spaces and symbols
# (!,@,#,$,%,&).
# To decode the script, Neo needs to read each column and select only
# the alphanumeric characters and connect them. Neo reads the column
# from top to bottom and starts reading from the leftmost column.
# If there are symbols or spaces between two alphanumeric characters of
# the decoded script, then Neo replaces them with a single space '' for
# better readability.
# Neo feels that there is no need to use 'if' conditions for decoding.
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].

import re

m, n = map(int, input().split())
arr=[]
for i in range(m):
    arr.append(list(input()))
s = ''.join([''.join(x) for x in list(zip(*arr))])
print(re.sub(r'(?<=[A-Za-z0-9])[ !@%&#\$]+(?=[A-Za-z0-9])',' ',s))