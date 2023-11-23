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
# rows = N + P

# for i in range(rows + 1):
#     if i <= N:
#         arr1 = np.array(list(map(int, input().split())))
#     else:
#         arr2 = np.array(list(map(int, input().split())))
# print(arr1)
# print(arr2)


# NxP MxP

# n=4
# m=3
# p=2

# [[1 2]
# [1 2]
# [1 2]
# [1 2]]

# [[3 4]
# [3 4]
# [3 4]]

# [[1 2]
# [1 2]
# [1 2]
# [1 2]
# [3 4]
# [3 4]
# [3 4]]
