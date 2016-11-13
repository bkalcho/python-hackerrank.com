# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Find angle from right triangle

import math

ab = int(input())
bc = int(input())
angle = math.atan2(ab, bc)
print(angle)
print(str(int(round(math.degrees(angle)))) + '°')