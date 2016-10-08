# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# Read a given string, change the character at a given index and then
# print the modified string.

s = input()
line = input()
i = int((line.split())[0])
c = (line.split())[1]
l = list(s)
l[i] = c
s = ''.join(l)
print(s)

# Another way, using list slices
#s = input()
#line = input()
#i = int((line.split())[0])
#c = (line.split())[1]
#s = s[:i] + c + s[i + 1:]
#print(s)