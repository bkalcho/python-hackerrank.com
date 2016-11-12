# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Find symetric difference of the 2 sets of integers.

m = int(input())
m_set = input()
m_set = m_set.split()
m_set = set(map(int, m_set))
n = int(input())
n_set = (input()).split()
n_set = set(map(int, n_set))
#####################################
m_diff_n = m_set.difference(n_set)
n_diff_m = n_set - m_set
mn_intersection = m_set & n_set
m_sym_diff_n = (m_diff_n.difference(mn_intersection)).union(n_diff_m.difference(mn_intersection))
######################################
# Another way is: m_sym_diff_n = m_set.symmetric_difference(n_set)
l = list(m_sym_diff_n)
ls = sorted(l, key=int)
for i in ls:
    print(i)