# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Check if A is strict superset of N subsets.

a, n = set(map(int, input().split())), int(input())
answ = True
for i in range(n):
    s = set(map(int, input().split()))
    if a.issuperset(s) and (a - s != set()):
        answ = answ and True
    else:
        answ = answ and False
        
print(answ)