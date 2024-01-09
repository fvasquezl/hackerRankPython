from collections import OrderedDict
if __name__ == "__main__":
    N = int(input())
    L1= OrderedDict()
    
    for i in range(N):
        a = list(map(str, input().split()))
        item_name = ' '.join(a[0:-1])
        net_price = int(a[-1])
        if L1.__contains__(item_name):
            net_price+=L1[item_name]
        L1[item_name] =  net_price
       
    for key,value in L1.items():
        print(key,value)
