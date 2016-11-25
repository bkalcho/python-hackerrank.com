# Author: Bojan G. Kalicanin
# Date: 25-Nov-2016
# You are given a valid XML document, and you have to print the maximum
# level of nesting in it. Take the depth of the root as 0.

import xml.etree.ElementTree as etree

def traverse(dept, node):
    if len(node)>0:
        dept = max(traverse(dept+1, x) for x in node)
    return dept

n = int(input())
xml_str = ''
for i in range(n):
    xml_str += input() + '\n'
tree = etree.ElementTree(etree.fromstring(xml_str))
root = tree.getroot()
print(traverse(0, root))