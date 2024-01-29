import email.utils
import re

if __name__ == "__main__":
    PATTERN = r"#[A-Fa-f\d]{3}(?:[A-Fa-f\d]{3})?\b"
    d = []
    for _ in range(int(input())):
        for i in re.finditer(PATTERN, input()):
            print(i.groups())
            d.append(i)

    # for i in d:
    #     p = email.utils.parseaddr(i)
    #     if bool(re.match(PATTERN, p[1])):
    #         print(email.utils.formataddr(p))

    print(d)
