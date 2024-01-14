"""Main Module"""
if __name__ == "__main__":
    K = int(input())
    r = sorted(list(map(int, input().split())))
    print((set(r[0::2]).symmetric_difference(set(r[1::2]))).pop())


# r =sort([1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2])
# Con el ordenamiento garantizamos que los elemento se distribuyan uniformemente en los dos sets que
# vamos a crear a continuacion

# r= [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,6,6,6,6,6,8]

# Extraer 2 listas, una de pares y otra de nones

# a[0::2] = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 8]
# a[1::2] = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 6, 6, 6]

# removemos duplicados

# set(a[0::2]) = {1, 2, 3, 4, 5, 6, 8}
# set(a[1::2]) = {1, 2, 3, 4, 5, 6}

# Discriminamos realizando una diferencia simetrica o XOR
# set((a[0::2]).symmetric_difference(set(r[0::2]).pop) = 8
