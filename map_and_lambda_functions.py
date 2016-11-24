# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You have to generate a list of the first N fibonacci numbers, 0 being
# the first number. Then, apply the map function and a lambda expression
# to cube each fibonacci number and print the list.

n = int(input())
l = list()
for i in range(n):
    if i == 0:
        l.append(i)
    elif i == 1:
        l.append(i)
    else:
        l.append(l[i-2] + l[i-1])
print(list(map(lambda x: x**3, l)))