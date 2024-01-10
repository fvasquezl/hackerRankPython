from collections import OrderedDict
if __name__ == "__main__":
    n = int(input())
    L1 = OrderedDict()
    for _ in range(n): 
        a= input()
        count = 1
        if L1.__contains__(a):
            count = L1[a] + 1
        L1[a] = count
    
    print(len(L1))
    print(*L1.values())

