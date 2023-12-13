# Complete the time_delta function below.
from collections import Counter

if __name__ == "__main__":
    s = int(input())
    ls = list(map(int, input().split()))
    l1 = Counter(ls)
    # for key, value in ls.items():
    #     print(key, value)

    c = int(input())
    lc = {}

    for c_itr in range(c):
        k, v = list(map(int, input().split()))
        if l1[k] != 0:
            print(l1[k])

    # print(shows(ls, lc))
