# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Convert complex number z to polar coordinates

import cmath

z = complex(input())
r = abs(z)
fi = cmath.phase(z)
print(r)
print(fi)