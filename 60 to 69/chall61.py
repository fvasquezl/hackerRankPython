if __name__ == "__main__":
    N1 = int(input())
    S1 = set(map(int, input().split()))
    N2 = int(input())
    S2 = set(map(int, input().split()))

    print(len(S1.intersection(S2)))
