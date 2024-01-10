from collections import deque

if __name__ == "__main__":
    N = int(input())
    L1 = deque()

    for _ in range(N):
        a = list(map(str, input().split()))
        if a[0] == "pop":
            L1.pop()
        if a[0] == "popleft":
            L1.popleft()
        elif a[0] == "append":
            L1.append(a[1])
        elif a[0] == "appendleft":
            L1.appendleft(a[1])

    print(*L1)


