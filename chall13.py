



if __name__ == '__main__':
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name,score])
        
    sorted_list = sorted(arr, key=itemgetter(1))

    print(sorted_list)
 