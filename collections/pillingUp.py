if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = list(map(int, input().split()))
        ch=[]
        res ='Yes'

        for _ in range(n):
            if s[-1]>=s[0]:
                ch.append(s[-1])
                s.pop()
            else:
                ch.append(s[0])
                s.pop(0)
        
            if len(ch)>1 and not ch[-2]>= ch[-1]:
                res='No'
                break
        print(res)
