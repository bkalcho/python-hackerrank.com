# Author: Bojan G. Kalicanin
# Date: 23-Nov-2016
# Compute the average scores of each student. The scores from X subjects
# are given for each of N students.

n, x = map(int, input().split())
scores_subject = list()
[scores_subject.append(map(float, input().split())) for i in range(x)]
a = list(zip(*scores_subject))
[print(sum(a[i])/len(a[i])) for i in range(n)]