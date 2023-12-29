import re

if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        a = input()
        try:
            re.compile(a)
            print(True)
        except re.error:
            print(False)
