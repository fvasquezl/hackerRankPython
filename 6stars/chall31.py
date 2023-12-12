#!/bin/python3

import datetime as dt
import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    res = dt.datetime.strptime(t1, format) - dt.datetime.strptime(t2, format)
    print(str(int(abs(res.total_seconds()))))

    return str(int(abs(res.total_seconds())))


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + "\n")

    fptr.close()
