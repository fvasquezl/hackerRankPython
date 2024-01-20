import re

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        S = input()
        print(str(bool(re.match(r"^([\-|\+]\d*|[\-|\+]|\d*)\.\d+$", S))))
