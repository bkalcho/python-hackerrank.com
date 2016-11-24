# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You are given a space separated list of integers. If all the integers
# are positive, then you need to check if any integer is a palindromic
# integer.

n, numbers = int(input()), list(map(int, input().split()))
print(all([i>0 for i in numbers]) and any([int(str(i)[::-1]) == i for i in numbers]))