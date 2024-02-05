import numpy

if __name__ == "__main__":
    N = int(input())
    a = []
    b = []
    for _ in range(N):
        a.append(list(map(int, (input().split()))))
    for _ in range(N):
        b.append(list(map(int, (input().split()))))
    A, B = numpy.array(a), numpy.array(b)

    print(numpy.dot(A, B))
