# Author: Bojan G. Kalicanin
# Date: 25-Nov-2016
# You are given N mobile numbers. Sort them in ascending order then
# print them in the standard format shown below.

def sort_mobile(numbers):
    numbers.sort()

n = int(input())
l = list()
[l.append(input()) for i in range(n)]

print(l)
sort_mobile(l)
print(l)