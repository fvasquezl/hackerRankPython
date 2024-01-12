from itertools import combinations

if __name__ == "__main__":
    N = int(input())
    L = list(map(str, input().split()))
    K = int(input())

    c = list(combinations(L, K))

    r = [x for x in c if x.__contains__("a")]

    print(len(r) / len(c))
