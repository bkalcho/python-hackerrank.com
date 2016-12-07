# Author: Bojan G. Kalicanin
# Date: 07-Dec-2016
# Your task is to validate whether P is a valid postal code or not.

import re

p = input()
print(bool(re.search(r'^[1-9][0-9]{5}$', p) and len(re.findall(r'(?=(\d)\d\1)', p))<2))