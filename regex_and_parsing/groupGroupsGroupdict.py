import re

if __name__ == "__main__":
    s = "..12345678910111213141516171820212223"
    m = "".join(re.findall(r"\w+", s))
    r = "-1"
    x = re.match(r"(1+)", m)
    for i in x:
        print(i.group())

    # for i in m:
    #     if len(re.findall(f"{i}+", m)) > 1:
    #         r = "1"
    #         break

    # print(r)
