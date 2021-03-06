# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# Read the integer, and print the decimal, octal, hexadecimal, and
# binary values from to with space padding so that all fields take the
# same width as the binary value.

n = int(input())
width = len("{0:b}".format(n))
for i in range(1, n + 1):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}". \
        format(i, width = width))