# Author: Bojan G. Kalicanin
# Date: 29-Nov-2016
# Let's use decorators to build a name directory! You are given some
# information about N people. Each person has a first name, last name,
# age and sex. Print their names in a specific format sorted by their
# age in ascending order i.e. the youngest person's name should be
# printed first. For two people of the same age, print them in the order
# of their input.

from operator import itemgetter

l = [input().split() for i in range(int(input()))]


def list_person(f):
    def inner(l):
        return [f(i) for i in sorted(l, key=itemgetter(2))]
    return inner

@list_person
def name_format(person):
    return ('Mr. ' if person[3] == 'M' else 'Ms. ') + person[0] + ' ' + person[1]

print(*name_format(l), sep='\n')