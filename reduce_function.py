# Author: Bojan G. Kalicanin
# Date: 08-Dec-2016
# Given a list of rational numbers,find their product.

from functools import reduce
from fractions import gcd, Fraction

def product(l):
    s = reduce(lambda x, y: x*y, l)
    return [s.numerator, s.denominator]


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    fracs[0].
    result = product(fracs)
    print(*result)

### SECOND SOLUTION without using fractions ###

#from functools import reduce
#from fractions import gcd

#n = int(input())
#rationals = []
#for i in range(n):
#    rationals.append(list(map(int, input().split())))
#s = [list(a) for a in zip(*rationals)]
#print(s)
#k = [reduce(lambda x, y: x*y, s[i]) for i in range(2)]
#c = reduce(gcd, k)
#for i in range(2):
#    k[i] //= c
#print(*k)