import re

if __name__ == "__main__":
    txt = "\n".join([input() for i in range(int(input()))])
    txt = re.sub("\s&{2}\s", " and ", txt)
    txt = re.sub("\s[|]{2}\s", " or ", txt)

    print(repr(txt))


        1

    x&& &&& && && x || | ||\|| x

x&& &&& and and x or | ||\|| x


x&& &&& and and x or | ||\|| x

c $&1|| or and and &|&&| & | | &&c

    1

    x&& &&& && && x || | ||\|| x

x&& &&& and and x or | ||\|| x