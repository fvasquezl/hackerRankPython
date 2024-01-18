"""Main Module"""
if __name__ == "__main__":
    n = input()
    l1 = list(map(int, input().split()))
    print(all(x > 0 for x in l1) and any(x for x in l1 if (str(x)[::-1]) == str(x)))
