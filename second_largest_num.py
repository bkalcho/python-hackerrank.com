# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# Find the second largest number

n = int(input())
line = input()
numbers = [int(x) for x in line.split()]
max_num = max(numbers)
numbers.sort(reverse=True)
number = numbers[0]
i = 1
while number >= max_num:
    number = numbers[i]
    i += 1
print(number)  