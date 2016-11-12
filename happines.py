# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Calculate your happines

n, m = tuple(map(int, (input()).split()))
ar = (input()).split()
ar = list(map(int, ar))
a = (input()).split()
a = set(map(int, a))
b = (input()).split()
b = set(map(int, b))

happines = 0
for i in ar:
    if i in a:
        happines += 1
    elif i in b:
        happines -= 1
print(happines)