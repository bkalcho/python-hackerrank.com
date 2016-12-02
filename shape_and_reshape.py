# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# You are given a space separated list of nine integers. Your task is to
# convert this list into a 3X3 NumPy array.

import numpy

a = numpy.array(list(map(int, input().split())), int)
a.shape = (3, 3)
print(a)