import re

if __name__ == "__main__":
    # REGEX = r"^(?=\d)(?!.*(\d)(?:-?\1){3})(?:[4|5|6])(?:\d{15}|\d{3}-.*\d{4})$"

    REGEX = r"^(?=\d)(?!.*(\d)(?:-?\1){3})(?:[4|5|6])(?:(?:\d{15})|(?:\d{3}(?:(?<=\d)-?)?\d{4}(?:(?<=\d)-?)?\d{4}(?:(?<=\d)-?)?\d{4}))$"

    result = []
    for _ in range(int(input())):
        OPTION = "Invalid"
        s = input()
        if bool(re.match(REGEX, s)):
            OPTION = "Valid"
        result.append(OPTION)
    for i in result:
        print(i)
