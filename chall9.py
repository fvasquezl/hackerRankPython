import numpy

values = tuple(int(i) for i in input().split())
arr0 = numpy.zeros(values, dtype=numpy.int_)
arr1 = numpy.ones(values, dtype=numpy.int_)

print(arr0)
print(arr1)
