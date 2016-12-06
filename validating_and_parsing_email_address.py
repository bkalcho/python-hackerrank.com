# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# Validate e-mail address

import re
import email.utils

pattern = re.compile('^[a-zA-Z][\w\.-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')
n = int(input())
for i in range(n):
    s = email.utils.parseaddr(input())
    m = pattern.match(s[1])
    if m:
        print(email.utils.formataddr(s))