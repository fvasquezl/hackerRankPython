def diff_students(l1, l2):
    x = l1.difference(l2)
    return len(x)


if __name__ == "__main__":
    t = int(input())
    l1 = set(map(int, input().split()))
    t2 = int(input())
    l2 = set(map(int, input().split()))

    print(diff_students(l1, l2))
