#!/bin/python3

import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
dd = ["!", "@", "#", "$", "%", "&"]
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = ""
k = 0
for i in range(m):
    for j in range(n):
        s += matrix[j][i]


print(*re.split("(?<=\w)\W+(?=\w)", s))
