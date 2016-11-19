# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# There is a horizontal row of n cubes. The length of each cube is
# given. You need to create a new vertical pile of cubes. The new pile
# should follow these directions: if cubeI is on top of cubeJ then
# sideLengthJ >= sideLengthI.
#
# When stacking the cubes, you can only pick up either the leftmost or
# the rightmost cube each time. Print "Yes" if it is possible to stack
# the cubes. Otherwise, print "No". Do not print the quotation marks.

from collections import deque

t = int(input()) # number of test cases
for i in range(t):
    n = int(input())
    sideLengths = deque()
    while len(sideLengths) < n:
        sideLengths.extend(map(int, input().split()))
    l = list()
    flag = True
    while sideLengths and flag:
        left = sideLengths[0]
        if len(sideLengths) > 1:
            right = sideLengths[-1]
            if len(l) > 0:
                if left >= right and left <= l[-1]:
                    left = sideLengths.popleft()
                    l.append(left)
                elif right > left and right <= l[-1]:
                    right = sideLengths.pop()
                    l.append(right)
                else:
                    flag = False
            else:
                if left >= right:
                    left = sideLengths.popleft()
                    l.append(left)
                else:
                    right = sideLengths.pop()
                    l.append(right)
        else:
            if len(l) > 0:
                if left <= l[-1]:
                    left = sideLengths.popleft()
                    l.append(left)
                else:
                    flag = False
    if flag:
        print('Yes')
    else:
        print('No')