import re

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        try:
            pattern = bool(re.compile("r'(" + input() + ")'"))
            print(pattern)
        except re.error:
            print("False")
