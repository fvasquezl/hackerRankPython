import numpy as np

arr1 = []
arr2 = []
n, m, p = list(map(int, input().split()))
for _ in range(n):
    arr1.append(list(map(int, input().split())))
for _ in range(m):
    arr2.append(list(map(int, input().split())))
result = np.concatenate((arr1, arr2), axis=0)

print(result)
