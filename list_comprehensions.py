# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# List comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())
# Using list comprehensions
result = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

#result = []
#for i in range(x + 1):
#    for j in range(y + 1):
#        for k in range(z + 1):
#            if i + j + k != n:
#                result.append([i, j, k])

print(result)