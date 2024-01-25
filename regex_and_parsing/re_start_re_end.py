import re

if __name__ == "__main__":
    # S = input()
    # K = input()
    S = "jjhv"
    K = "z"
    r = re.compile(rf"(?=({K}))")
    m = list(re.finditer(r, S))

    if m:
        for i in m:
            print(tuple([i.start(), i.end() + (len(K) - 1)]))
    else:
        print("(-1,-1)")
