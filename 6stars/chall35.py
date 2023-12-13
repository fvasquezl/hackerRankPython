from collections import defaultdict

if __name__ == "__main__":
    a, b = list(map(int, input().split()))
    l1 = defaultdict(list)
    l2 = defaultdict(list)

    for i in range(a):
        a = input()
        l1[a].append(i + 1)

    for i in range(b):
        b = input()
        if l1[b]:
            l2[i].append(" ".join(str(e) for e in l1[b]))
        else:
            l2[i].append("-1")
    for i in l2.values():
        print(*i)
