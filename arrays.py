# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# You are given a space separated list of numbers. Your task is to print
# a reversed NumPy array with the element type float.

import numpy

a = numpy.array(list(map(float, input().split())), float)
print(a[::-1])