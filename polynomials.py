# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given the coefficients of a polynomial P. Your task is to find
# the value of P at point x.

import numpy

a = list(map(float, input().split()))
x = float(input())
print(numpy.polyval(a, x))