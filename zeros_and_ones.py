# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# Your task is to print an array of size N and integer type using the
# tools zeros and ones. N is the space separated list of the dimensions
# of the array.

import numpy

a = tuple(map(int, input().split()))
print(numpy.zeros(a, dtype=numpy.int))
print(numpy.ones(a, dtype=numpy.int))