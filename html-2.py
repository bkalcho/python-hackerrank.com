# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given an HTML code snippet of N lines. Your task is to print
# the single-line comments, multi-line comments and the data.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)
            
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

n = int(input())
lines = list()
for i in range(n):
    lines.append(input())
s = '\n'.join(lines)

parser = MyHTMLParser()
parser.feed(s)