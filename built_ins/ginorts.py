"""Main Module"""

import re


def sorting(x):
    return x.lower()


if __name__ == "__main__":
    r = []
    s = input()

    l = sorted(re.findall(r"[a-z]", s))
    L = sorted(re.findall(r"[A-Z]", s))
    n = sorted(re.findall(r"\d", s))
    o = [x for x in n if int(x) % 2 != 0]
    e = [x for x in n if int(x) % 2 == 0]
    print("".join(l + L + o + e))
