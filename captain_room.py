# Author: Bojan G. Kalicanin
# Date: 12-Nov-2016
# Find a captain's room.

k = int(input())
room_numbers = list(map(int, input().split()))
distinct_rooms = set(room_numbers)
print(((sum(distinct_rooms)*k)-(sum(room_numbers)))//(k-1))