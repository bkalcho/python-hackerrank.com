# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Count the total number of distinct country stamps in a collection.

n = int(input())
d_stamps = set()
for i in range(n):
    d_stamps.add(input())
print(len(d_stamps))