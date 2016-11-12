# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Execute N commands given in N lines.

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    string = (input()).split()
    comm = string[0]
    if len(string) == 2:
        arg = int(string[1])
        exe_str = 's.' + comm + '(' + str(arg) + ')'
        exec(exe_str)
    else:
        exe_str = 's.' + comm + '()'
        exec(exe_str)
        
print(sum(s))