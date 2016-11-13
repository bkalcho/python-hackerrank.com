# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Make aplindromic triangle

for i in range(1, int(input()) + 1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(((10**i-1)//9)**2)
    
# Alternative
#print(('').join([ str(x) for x in range(1, i+1)] + [ str(x) for x in range(i-1, 0, -1)]))