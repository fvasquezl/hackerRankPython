if __name__ == "__main__":
    K = int(input())
    r = list(map(int, input().split()))
    print((set(r[0::2]) ^ set(r[1::2])).pop())

    print(set(r[0::2]).symmetric_difference(set(r[1::2])).pop())


'''
r =[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
print((set(r[0::2]) ^ set(r[1::2])).pop())

a[0::2] = [1, 3, 5, 4, 5, 6, 6, 3, 4, 2, 1, 3, 8, 3, 5, 2]
a[1::2] = [2, 6, 4, 2, 3, 1, 5, 2, 1, 5, 4, 6, 4, 1, 6]

set(a[0::2]) = {1, 2, 3, 4, 5, 6, 8}
set(a[1::2]) = {1, 2, 3, 4, 5, 6}

set(a[0::2]).symmetric_difference(set(r[0::2]) = {8}

'''
