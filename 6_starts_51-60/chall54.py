import numpy

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(1, n + 1):
        a.append(list(map(float, input().split())))

    print(numpy.around(numpy.linalg.det(a), 2))
