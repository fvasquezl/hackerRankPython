"""algo aqui"""
import re

if __name__ == "__main__":
    PATTERN = r"#[A-Fa-f\d]{3}(?:[A-Fa-f\d]{3})?\b"
    TXT = ""
    d = []

    for _ in range(int(input())):
        TXT += input()

    m = re.finditer(r"\{.*?\}", TXT)
    if m:
        for i in m:
            n = re.finditer(PATTERN, i.group())
            if n:
                for j in n:
                    d.append(j.group())
    for i in d:
        print(i)
