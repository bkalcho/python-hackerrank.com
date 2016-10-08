# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# Given the names and grades for each student in a Physics class of
# students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

n = int(input())
data = [[input(), float(input())] for i in range(n)]

for i in range(1, n):
    for j in range(n - 1):
        if data[j][1] > data[j + 1][1]:
            t = data[j]
            data[j] = data[j + 1]
            data[j + 1] = t 

i = 0
while data[i + 1][1] <= data[i][1]:
    i += 1
s_lowest = data[i + 1][1]
names = []
for i in range(n):
    if data[i][1] == s_lowest:
        names.append(data[i][0])

names.sort()
for name in names:
    print(name)