# Author: Bojan G. Kalicanin
# Date: 07-Dec-2016
# You and Fredrick are good friends. Yesterday, Fredrick received N
# credit cards from ABCD Bank. He wants to verify whether his credit
# card numbers are valid or not. You happen to be great at regex so he
# is asking for your help!

import re

n = int(input())
for i in range(n):
    s = input()
    if re.match(r'^[456]\d{3}(?:-?\d{4}){3}$', s) and not re.search(r'(\d)\1{3}', re.sub('-', '', s)) and not re.search(r'[\s_]', s):
        print('Valid')
    else:
        print('Invalid')