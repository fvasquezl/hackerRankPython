if __name__ == "__main__":
    n = int(input())
    l1 = []
    for _ in range(n):
        l1.append(list(map(str, input().split())))

    for i in l1:
        try:
            print(int(i[0]) // int(i[1]))
        except ZeroDivisionError:
            print("Error Code:", "integer division or modulo by zero")
        except ValueError as e:
            print("Error Code:", e)
