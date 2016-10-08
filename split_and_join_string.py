# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# You are given a string. Split the string on a " " (space) delimiter
# and join using a - hyphen.

string = input()
str_list = string.split(" ")
print("-".join(str_list))