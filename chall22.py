if __name__ == "__main__":
    s = input()
    op = [0,0,0,0,0]

    for i in s:
        if i.isalnum() and op[0] == 0 :
            op[0]=1
        if i.isalpha() and op[1] == 0:
            op[1]=1
        if i.isdigit() and op[2] == 0:
            op[2]=1
        if i.islower() and op[3] == 0:
            op[3]=1
        if i.isupper() and op[4] == 0:
            op[4]=1
        if (op==[1,1,1,1,1]):
            break
        
    for i in op:
        print(bool(i))
