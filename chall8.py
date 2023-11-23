import numpy as np

N, M, P = list(map(int, input().split()))
# arr1=[]
# arr2=[]
rows = N+P

for i in range(rows+1):
    if i<=N:
        arr1 = np.array(list(map(int, input().split()))) 
    else:
        arr2 = np.array(list(map(int, input().split()))) 
print(arr1)
print(arr2)





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