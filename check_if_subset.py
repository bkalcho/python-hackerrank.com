# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Check if set A is a subset of set B.

t = int(input())
for i in range(t):
    a_n = int(input())
    a = set(map(int, input().split()))
    b_n = int(input())
    b = set(map(int, input().split()))
    if a.intersection(b) == a:
        print(True)
    else:
        print(False)