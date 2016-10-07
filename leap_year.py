# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Check if year is leap or not

def is_leap(year):
    leap = False
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        leap = True
    else:
        leap = False

    return leap

year = int(input("Enter year: "))
print("Is year " + str(year) + " leap?")
print(is_leap(year))