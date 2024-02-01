import numpy

if __name__ == "__main__":
    n, m = map(int, (input().split()))
    l1 = []
    for i in range(n):
        l1.append(list(map(int, (input().split()))))
    arr = numpy.array(l1)
    print(numpy.transpose(arr))
    print(arr.flatten())
