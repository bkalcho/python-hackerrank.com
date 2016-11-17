# Author: Bojan G. Kalicanin
# Date: 17-Nov-2016
# In this challenge, you will be given 2 integers, n and m. There are n
# words, which might repeat, in word group A. There are m words
# belonging to word group B. For each m words, check whether the word
# has appeared in group A or not. Print the indices of each occurrence
# of m in group A. If it does not appear, print -1.

from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)
[a[input()].append(i) for i in range(1, n+1)]
b = list()
[b.append(input()) for i in range(m)]
[[[print(a[b[i]][j], end=' ') for j in range(len(a[b[i]]))], print()] if b[i] in a else print(-1) for i in range(m)]