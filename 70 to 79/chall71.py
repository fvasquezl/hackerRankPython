if __name__ == "__main__":
    n = int(input())
    n_set = set(map(int, input().split()))
    b = int(input())
    b_set = set(map(int, input().split()))

    print(len(n_set.union(b_set)))
