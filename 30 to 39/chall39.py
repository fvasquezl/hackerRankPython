from itertools import groupby

if __name__ == "__main__":
    a = str(input())
    li = []
    for k, v in groupby(a):
        li.append((len(list(v)), int(k)))

    print(*li)
