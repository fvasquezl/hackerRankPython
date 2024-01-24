import re

if __name__ == "__main__":
    S = "__commit__"
    m = re.match(r".*?([A-Za-z0-9])\1.*", S)

    if m:
        print(m.group(1))
    else:
        print("-1")

    # if m.group(1):
    #     print(m.group(1))
    # else:
    #     print(-1)
