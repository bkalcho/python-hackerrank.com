# Author: Bojan G. Kalicanin
# Date: 07-Oct-2016
# Read input and convert it to a list

lst = []
n = int(input())
for i in range(0, n):
    line = input()
    commands = line.split()

    if commands[0] == 'insert':
        lst.insert(int(commands[1]), int(commands[2]))
    elif commands[0] == 'print':
        print(lst)
    elif commands[0] == 'remove':
        lst.remove(int(commands[1]))
    elif commands[0] == 'append':
        lst.append(int(commands[1]))
    elif commands[0] == 'sort':
        lst.sort()
    elif commands[0] == 'pop':
        lst.pop()
    elif commands[0] == 'reverse':
        lst.reverse()