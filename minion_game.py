# Author: Bojan G. Kalicanin
# Date: 10-Nov-2016
# The Minion Game: Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# A player gets +1 point for each occurrence of the substring in the
# string S.
# The string S will contain only uppercase letters: [A-Z].

s = input("Enter string: ")

vowels = 'AEIOU'

kevin_score = 0
stuart_score = 0
for i in range(len(s)):
    if s[i] in vowels:
        kevin_score += (len(s) - i)
    else:
        stuart_score += (len(s) - i)
        
if kevin_score > stuart_score:
    print("Kevin", kevin_score)
elif kevin_score < stuart_score:
    print("Stuart", stuart_score)
else:
    print("Draw")