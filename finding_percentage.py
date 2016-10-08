# Author: Bojan G. Kalicanin
# Date: 08-Oct-2016
# You have a record of students. Each record contains the student's
# name, and their percent marks in Maths, Physics and Chemistry. 
# The marks can be floating values. The user enters some integer 
# followed by the names and marks for students. You are required to
# save the record in a dictionary data type. The user then enters a
# student's name. Output the average percentage marks obtained by that
# student, correct to two decimal places.

dict = {}
n = int(input())
for i in range(n + 1):
    line = input()
    if i == n:
        break
    student_info = line.split()
    percentage = []
    dict[student_info[0]] = [
        float(student_info[1]),
        float(student_info[2]),
        float(student_info[3])
        ]

for key, value in dict.items():
    if key == line.strip():
        sum = 0
        for num in value:
            sum += num
        percentage = sum / len(value)

# new string format syntax, introduced in Python 3.1
print("{:.2f}".format(percentage))
# String formant printf style, valid for python 2.7
#print("%.2f" % percentage)