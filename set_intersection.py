# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Find total number of the students subscribed to both newspaper.

n = int(input()) # number of students subscribed to the English newspaper
n_roll = set(map(int, input().split()))
b = int(input()) # number of students subscribed to the French newspaper
b_roll = set(map(int, input().split()))
print(len(n_roll.intersection(b_roll)))