# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# You are given a string .
# Your task is to find out if the string contains: alphanumeric
# characters, alphabetical characters, digits, lowercase and uppercase
# characters.

s = list(input())
lst = []

flag = False
for c in s:
    if c.isalnum():
        flag = True
lst.append(flag)

flag = False
for c in s:
    if c.isalpha():
        flag = True
lst.append(flag)

flag = False
for c in s:
    if c.isdigit():
        flag = True
lst.append(flag)


flag = False
for c in s:
    if c.islower():
        flag = True
lst.append(flag)

flag = False
for c in s:
    if c.isupper():
        flag = True
lst.append(flag)

for l in lst:
    print(l)