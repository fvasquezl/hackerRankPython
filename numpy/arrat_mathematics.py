import numpy

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    arr_a = []
    arr_b = []
    for _ in range(n):
        arr_a.append(list(map(int, input().split())))
    for _ in range(n):
        arr_b.append(list(map(int, input().split())))
    a = numpy.array(arr_a)
    b = numpy.array(arr_b)

    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))
