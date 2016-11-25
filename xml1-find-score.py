# Author: Bojan G. Kalicanin
# Date: 25-Nov-2016
# You are given a valid XML document, and you have to print its score.
# The score is calculated by the sum of the score of each element. For
# any element, the score is equal to the number of attributes it has.

import xml.etree.ElementTree as etree

n = int(input())
xml_str = ''
for i in range(n):
    xml_str += input() + '\n'
tree = etree.ElementTree(etree.fromstring(xml_str))
print(sum([len(i.attrib) for i in tree.iter()]))