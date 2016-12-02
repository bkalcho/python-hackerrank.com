# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given a 2-D array with dimensions NxM. Your task is to perform
# the min function over axis 1 and then find the max of that.

import numpy

n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.max(numpy.min(a, 1)))