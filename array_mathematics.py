# Author: Bojan G. Kalicanin
# Date: 01-Dec-2016
# You are given two arrays (A & B) of dimensions NxM.
# Your task is to perform the following operations:
#
#    1. Add(A + B)
#    2. Subtract(A - B)
#    3. Multiply(A * B)
#    4. Divide (A / B)
#    5. Mod(A % B)
#    Power (A ** B)

import numpy

n, m = map(int, input().split())
a = numpy.array([map(int, input().split()) for i in range(n)])
b = numpy.array([map(int, input().split()) for i in range(n)])

print(a+b)
print(a-1)
print(a*b)
print(numpy.div(A, B))
print(a%b)
print(a**b)