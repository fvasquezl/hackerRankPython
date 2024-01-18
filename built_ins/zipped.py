if __name__ == "__main__":
    r = []
    n, x = list(map(int, input().split()))

    for i in range(1, x + 1):
        r.append(list(map(float, input().split())))

    for i in zip(*r):
        print(sum(i) / x)
    # print(zip(*r))
"""
5 3
89 90 78 93 80
90 91 85 88 86
91 92 83 89 90.5
"""
