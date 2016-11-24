# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You are given a polynomial P of a single indeterminate (or variable),
# x. You are also given the values of x and . Your task is to verify if
# P(x) = k.

x, k = map(int, input().split())
print(eval(input()) == k)