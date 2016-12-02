# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given a 2-D array of size NxM.
# Your task is to find:
#
#   1. The mean along axis 1.
#   2. The var along axis 0.
#   3. The std along axis None.

import numpy

n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.std(a))