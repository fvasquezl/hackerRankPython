N, M = map(int, input().split())
z = ".|."
j = 1
i = 1
while i < N + 1:
    if i == (N + 1) / 2:
        print(("WELCOME").center(M, "-"))
        j -= 2
    else:
        print((z * j).center(M, "-"))
        if i < (N + 1) / 2:
            j += 2
        elif i > (N + 1) / 2:
            j -= 2
    i += 1
