# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Compute the average of all the plants with distinct heights.

n = input() # Number of all plants in the greenhouse
h = input() # heights of all plants
h = set([int(x) for x in h.split()]) # distinct heights of plants
avg = sum(h) / len(h)
print(avg)