import re

if __name__ == "__main__":
    S = input()
    # S = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
    # S = "match a single character not present in the list below"
    r = re.compile(
        r"(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])"
    )

    m = list(map(lambda x: x.group(), re.finditer(r, S)))

    if m:
        for i in m:
            print(i)
    else:
        print("-1")
