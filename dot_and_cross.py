# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given two arrays A and B. Both have dimensions of NxN. Your
# task is to compute their matrix product.

import numpy

n = int(input())
a = numpy.array([list(map(int, input().split())) for i in range(n)])
b = numpy.array([list(map(int, input().split())) for i in range(n)])
print(numpy.dot(a, b))