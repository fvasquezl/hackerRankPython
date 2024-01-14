"""Main Module"""
if __name__ == "__main__":
    A = int(input())
    A_set = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        a = list(map(str, input().split()))
        data = set(map(int, input().split()))
        if a[0] == "intersection_update":
            A_set.intersection_update(data)
        elif a[0] == "update":
            A_set.update(data)
        elif a[0] == "symmetric_difference_update":
            A_set.symmetric_difference_update(data)
        elif a[0] == "difference_update":
            A_set.difference_update(data)

    print(sum(A_set))
