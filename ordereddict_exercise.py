# Author: Bojan G. Kalicanin
# Date: 18-Nov-2016
# You are the manager of a supermarket.
# You have a list of N items together with their prices that consumers
# bought on a particular day. Your task is to print each item_name and
# net_price in order of its first occurrence.

from collections import OrderedDict

n = int(input())
items_ = OrderedDict()
for i in range(n):
    item_n, space, item_p = input().rpartition(' ')
    if item_n in items_:
        items_[item_n] += int(item_p)
    else:
        items_[item_n] = int(item_p)
for item_name, net_price in items_.items():
    print(item_name + " " + str(net_price))