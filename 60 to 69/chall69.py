#!/bin/python3

from collections import Counter


if __name__ == "__main__":
    s = input()

    l1 = Counter(sorted(s)).most_common(3)

    for i in l1:
        print(*i)
