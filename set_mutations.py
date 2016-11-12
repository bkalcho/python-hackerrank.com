# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
#

a_num = int(input())
a = set(map(int, input().split()))
n = int(input())
for i in range(n):
    string = input().split()
    comm = string[0]
    set_n = int(string[1])
    set_l = set(map(int, input().split()))
    exe_str = 'a' + '.' + comm + '(' + 'set_l' + ')'
    exec(exe_str)
    
print(sum(a))