import math
import os
import random
import re
import sys

if __name__ == "__main__":
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in list(sorted(arr, key=lambda p: p[k])):
        print(*i)
