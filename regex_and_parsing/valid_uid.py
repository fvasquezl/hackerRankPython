import re

if __name__ == "__main__":
    result = []
    for _ in range(int(input())):
        option = "Invalid"
        s = input()
        if (
            bool(re.match(r"^([A-Za-z\d]{10})$", s))
            and len(re.findall(r"[A-Z]", s)) >= 2
            and len(re.findall(r"[\d]", s)) >= 3
            and len(re.findall(r"(?:(.)(?=.*\1))", s)) == 0
        ):
            option = "Valid"
        result.append(option)
    for i in result:
        print(i)
