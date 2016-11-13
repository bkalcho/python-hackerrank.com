# Author: Bojan G. Kalicanin
# Date: 13-Nov-2016
# Print a numerical triangle

for i in range(1, int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)*2)