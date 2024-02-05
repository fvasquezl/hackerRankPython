import numpy

if __name__ == "__main__":
    N, M = list(map(int, (input().split())))
    a = []
    for _ in range(N):
        a.append(list(map(int, (input().split()))))
    A = numpy.array(a)

    print(numpy.mean(numpy.min(A, axis=1)))
