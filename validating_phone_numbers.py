# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# Let's dive into the interesting topic of regular expressions!
# You are given some input, and you are required to check whether they
# are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7, 8 or 9.

import re

pattern = re.compile('^[789]\d{9}$')
n = int(input())
[print('YES') if pattern.match(input()) else print('NO') for i in range(n)]