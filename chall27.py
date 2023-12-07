import string


def print_rangoli(size):

    L = list(map(chr, range(97, size+97)))
    M = len(L)*2-1
    j=0
    k=-1

    for _ in range(M):
        r = L[j:]
        e = list(reversed(r))[:k]
        print(e,r)
        j+=1
        k-=1

   
    # for _ in range(list(map(chr, range(97, 123)))):
    #     print("text","-")
    
    return

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)