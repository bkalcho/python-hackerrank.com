# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# You are given two values a and b.
# Perform integer division and print a/b.

for i in range(int(input())):
    try:
        l = list(map(int, input().split()))
        print(l[0] // l[1])
    except ZeroDivisionError as z:
        print("Error Code:", z)
    except ValueError as v:
        print("Error Code:", v)