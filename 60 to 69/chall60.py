if __name__ == "__main__":
    A = set(map(int, input().split()))
    r = True
    for n in range(int(input())):
        if A.issuperset(set(map(int, input().split()))) is False:
            r = False

    print(r)
