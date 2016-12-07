# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given an HTML code snippet of N lines. Your task is to detect
# and print all the HTML tags, attributes and attribute values.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr, val in attrs:
                print("-> " + attr + " > " + val)

n = int(input())
lines = list()
for i in range(n):
    lines.append(input())
s = '\n'.join(lines)

parser = MyHTMLParser()
parser.feed(s)