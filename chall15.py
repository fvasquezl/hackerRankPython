if __name__ == "__main__":
    arr = []
    out =[]
    N = int(input())
    for _ in range(N):
        el = input().split()
        arr.append(el)

    for action in arr:
        if action[0] == 'insert':
            op1= int(action[1])
            op2= int(action[2])
            out.insert(op1,op2)
        elif action[0] == 'remove':
            op1= int(action[1])
            out.remove(op1)
        elif action[0] == 'append':
            op1= int(action[1])
            out.append(op1)
        elif action[0] == 'sort':
            out.sort()
        elif action[0] == 'pop':
            out.pop()
        elif action[0] == 'reverse':
            out.reverse()
        else:
            print(out)