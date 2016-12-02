# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given a 2-D array with dimensions NxM.
# Your task is to perform the sum tool over axis 0 and then find the
# product of that result.

import numpy

n, m = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.prod(numpy.sum(a, axis=0)))