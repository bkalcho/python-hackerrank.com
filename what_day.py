# Author: Bojan G. Kalicanin
# Date: 19-Nov-2016
# You are given a date. Your task is to find what the day is on that date.
import calendar

enum = [
        'MONDAY',
        'TUESDAY',
        'WEDNESDAY',
        'THURSDAY',
        'FRIDAY',
        'SATURDAY',
        'SUNDAY'
        ]

date_str = list(map(int, input().split()))
day = calendar.weekday(date_str[2], date_str[0], date_str[1])
print(enum[day])