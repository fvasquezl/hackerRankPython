if __name__ == "__main__":
    A = int(input())
    A_set = set(map(int, input().split()))
    N = int(input())
    # for _ in range(2 * N):
    #     a = list(map(str, input().split()))
    #     data = set(map(int, input().split()))
    #     if a[0] == "intersection_update":
    #         A_set.intersection_update(a[1])
    #     elif a[0] == "update":
    #         A_set.update(a[1])
    #     elif a[0] == "symmetric_difference_update":
    #         A_set.symmetric_difference_update(a[1])
    #     elif a[0] == "difference_update":
    #         A_set.difference_update(a[1])

    print(A_set)
