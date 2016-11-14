# Author: Bojan G. Kalicanin
# Date: 14-Nov-2016
# Calculate max value of S = (f(x1) + f(x2) + ... + f(xk))%M

from itertools import product

def polynomial(numbers):
    return sum(x*x for x in numbers)%m

k, m = map(int, input().split())
arrays = []
for i in range(k):
    arrays.append(map(int, input().split())[1:]) # Append arrays without the first elements. We got one Array which elements are arrays

combinations = list(product(*arrays))
print(max(list(map(polynomial, combinations))))