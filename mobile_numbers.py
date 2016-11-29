# Author: Bojan G. Kalicanin
# Date: 26-Nov-2016
# You are given N mobile numbers. Sort them in ascending order then
# print them in the standard format shown below.

l = [input() for i in range(int(input()))]

def wrapper(f):
    def format_numbers(l):
        f(['+91 ' + i[-10:-5] + ' ' + i[-5:] for i in l])
    return format_numbers

@wrapper
def sort_mobile(numbers):
    print(*sorted(numbers), sep='\n')

sort_mobile(l)