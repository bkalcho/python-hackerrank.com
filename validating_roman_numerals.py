# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given a string, and you have to validate whether it's a valid
# Roman numeral. If it is valid, print True. Otherwise, print False.
# Try to create a regular expression for a valid Roman numeral.

import re

s = input()
p = re.compile('M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
print(bool(p.match(s)))