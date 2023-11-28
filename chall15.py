if __name__ == "__main__":
    arr = []
    out =[]
    N = int(input())
    for _ in range(N):
        el = input().split()
        arr.append(el)

    for action in arr:
        match action[0]:
            case "insert":
                op1= int(action[1])
                op2= int(action[2])
                out.insert(op1,op2)
            case  'remove':
                op1= int(action[1])
                out.remove(op1)
            case 'append':
                op1= int(action[1])
                out.append(op1)
            case 'sort':
                out.sort()
            case 'pop':
                out.pop()
            case 'reverse':
                out.reverse()
            case 'print':
                print(out)
                