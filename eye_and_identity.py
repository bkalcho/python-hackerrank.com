# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# Your task is to print an array of size NxM with its main diagonal
# elements as 1's and 0's everywhere else.

import numpy

n, m = map(int, input().split())
print(numpy.eye(n, m))