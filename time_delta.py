# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# Given 2 timestamps, print the absolute difference (in seconds) between
# them.
import datetime

format = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    diff = datetime.datetime.strptime(input(), format) - datetime.datetime.strptime(input(), format)
    print(int(abs(diff.total_seconds())))