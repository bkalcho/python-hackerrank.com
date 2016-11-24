# Author: Bojan G. Kalicanin
# Date: 24-Nov-2016
# You are given a string S. S contains alphanumeric characters only.
# Your task is to sort the string S in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.

order_of_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order_of_characters.index), sep='')