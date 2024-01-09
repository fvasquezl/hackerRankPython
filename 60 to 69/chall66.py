# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    for _ in range(N):
        a = list(map(str, input().split()))
        if a[0] == "pop":
            s.pop()
        elif a[0] == "remove":
            s.remove(int(a[1]))
        elif a[0] == "discard":
            s.discard(int(a[1]))

    print(sum(s))
