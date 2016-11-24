# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You are given an integer N followed by N email addresses. Your task is
# to print a list containing only valid email addresses in
# lexicographical order.
# Valid email addresses must follow these rules:
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores.
# The website name can only have letters and digits.
# The maximum length of the extension is 3.

import re

e_mail_address = re.compile("^[\w-]{1,}@[a-zA-Z0-9]{1,}\.\w{1,3}$", re.UNICODE)
print(sorted(filter(e_mail_address.search, (input() for i in range(int(input()))))))