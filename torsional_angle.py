# Author: Bojan G. Kalicanin
# Date: 20-Nov-2016
#

from math import sqrt, acos, degrees

class Vector(object):
    """Representation of the vector."""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def dot(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def cross(self, other):
        return Vector(
                        self.y*other.z - self.z*other.y,
                        self.z*other.x - self.x*other.z,
                        self.x*other.y - self.y*other.x
                     )

    def mod(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

if __name__ == '__main__':
    A = Vector(*map(float, input().split()))
    B = Vector(*map(float, input().split()))
    C = Vector(*map(float, input().split()))
    D = Vector(*map(float, input().split()))
    AB = B - A
    BC = C - B
    CD = D - C
    X = AB.cross(BC)
    Y = BC.cross(CD)
    print("{0:.2f}".format(degrees(acos(X.dot(Y)/X.mod()/Y.mod()))))