# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You are given data in a tabular format. The data contains N rows, and
# each row contains M space separated elements. You can imagine the M
# items to be different attributes, (like height, weight, energy, etc.)
# and each of the N rows as an instance or a sample. Your task is to
# sort the table on the K-th attribute and print the final resulting
# table.
# Note: If two attributes are the same for different rows, print the row
# that appeared first in the input.

n, m = map(int, input().split())
l = list()
for i in range(n):
    l.append(list(map(int, input().split())))
k = int(input())
for i in sorted(l, key=lambda x: x[k]):
    print(*i)