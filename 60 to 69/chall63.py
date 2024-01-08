if __name__ == "__main__":
    N, M = map(int, input().split())
    L1 = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    like = 0
    for i in L1:
        if i in A:
            like += 1
        if i in B:
            like -= 1

    print(like)
