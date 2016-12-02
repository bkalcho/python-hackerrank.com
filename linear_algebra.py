# Author: Bojan G. Kalicanin
# Date: 02-Dec-2016
# You are given a square matrix A with dimensions NxN. Your task is to
# find the determinant.

import numpy

n = int(input())
a = [list(map(float, input().split())) for i in range(n)]
print(numpy.linalg.det(a))