import numpy

if __name__ == "__main__":
    A = list(map(float, input().split()))
    B = list(map(int, input().split()))

    print(*numpy.polyval(A, B))
