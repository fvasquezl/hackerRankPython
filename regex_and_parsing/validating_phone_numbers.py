import re

if __name__ == "__main__":
    N = list([input() for i in range(int(input()))])
    for i in N:
        if bool(re.match(r"^(?:7|8|9)(?:\d{9})$", i)):
            print("YES")
        else:
            print("NO")
