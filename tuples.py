# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# Create a tuple

n = input()
line = input()
# Create tuple from the line
tpl = tuple(int(x) for x in line.split())

# Another way to do it using map() function
# tpl = tuple(map(int, line.split()))
# Same but create a list
# numbers = list(map(int, line.split()))
print(hash(tpl))