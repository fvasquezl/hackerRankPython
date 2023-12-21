# Complete the time_delta function below.
from collections import Counter

if __name__ == "__main__":
    lc = {}
    profit = 0
    s = int(input())
    ls = list(map(int, input().split()))
    l1 = Counter(ls)
    c = int(input())
    for c_itr in range(c):
        k, v = list(map(int, input().split()))
        if l1[k] != 0:
            l1[k] -= 1
            profit += v

    print(profit)
