# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# In this challenge, the user enters a string and a substring. You have
# to print the number of times that the substring occurs in the given
# string. String traversal will take place from left to right, not from
# right to left.

s = input()
s1 = input()
j = len(s1)
i = 0
k = 0
while j <= len(s):
    if s[i:j] == s1:
        k += 1
    j += 1
    i += 1
print(k)