if __name__ == "__main__":
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    x = 1
    y = 1
    z = 2
    n = 3

    print(
        [
            [i, j, k]
            for i in range(x + 1)
            for j in range(y + 1)
            for k in range(z + 1)
            if sum([i, j, k]) != n
        ]
    )

    # print(r)

    # r1 = [list(i) for i in itertools.product(x1, y1, z1)]

    # print(r1)
