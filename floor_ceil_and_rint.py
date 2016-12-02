# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given a 1-D array, A. Your task is to print the floor, ceil
# and rint of all the elements of A.

import numpy

a = numpy.array(list(map(float, input().split())))
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))