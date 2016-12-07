# Author: Bojan G. Kalicanin
# Date: 06-Dec-2016
# You are given an HTML code snippet of N lines. Your task is to print
# start tags, end tags and empty tags separately.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start : " + tag)
        self.value(attrs)

    def handle_endtag(slef, tag):
        print("End   : " + tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty : " + tag)
        self.value(attrs)

    def value(self, attrs = None):
        if attrs:
            [print('->', attr, '>', val) for attr, val in attrs]

n = int(input())
lines = list()
for i in range(n):
    lines.append(input())
s = '\n'.join(lines)
parser = MyHTMLParser()
parser.feed(s)