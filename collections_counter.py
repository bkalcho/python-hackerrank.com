# Author: Bojan G. Kalicanin
# Date: 17-Nov-2016
# Raghu is a shoe shop owner. His shop has X number of shoes. He has a
# list containing the size of each shoe he has in his shop. There are N
# number of customers who are willing to pay xi amount of money only if
# they get the shoe of their desired size.
# Your task is to compute how much money Raghu earned.

from collections import Counter

X = int(input()) # number of shoes in the store
shoe_sizes = list(map(int, input().split())) # list of all shoe sizes
d = Counter(shoe_sizes)
N = int(input()) # number of customers
request_shoes = {}
available_offer = []
for i in range(N):
    shoe_size, shoe_price = map(int, input().split())
    if shoe_size in d and d[shoe_size] > 0:
        available_offer.append(shoe_price)
        d[shoe_size] -= 1
print(sum(available_offer))