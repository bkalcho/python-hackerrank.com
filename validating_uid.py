# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# ABCXYZ company has up to 100 employees.
# The company decides to create a unique identification number (UID) for
# each of its employees. The company has assigned you the task of
# validating all the randomly generated UIDs.

import re

for i in range(int(input())):
    s = input()
    print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}', r'([A-Z].*){2}', r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid') 