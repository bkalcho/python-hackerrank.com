# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# You are given two integer arrays of size NxP and MxP (N&M are rows,
# and P is the column). Your task is to concatenate the arrays along
# axis 0.

import numpy

n, m, p = map(int, input().split())
a = numpy.array([list(map(int, input().split())) for i in range(n)])
b = numpy.array([list(map(int, input().split())) for i in range(m)])
print(numpy.concatenate((a, b)))