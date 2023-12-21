from itertools import combinations

if __name__ == "__main__":
    a, b = map(str, input().split())
    for i in range(1, int(b) + 1):
        for j in list(combinations(sorted(a), i)):
            print("".join(j))
