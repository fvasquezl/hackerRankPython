if __name__ == "__main__":
    s = input()
    a, b, c, d, e : bool
    for i in s:
        if i.isalnum() and a == True:
            print(i.isalnum())
            a = False
        elif i.isalpha() and b:
            print(i.isalpha())
            b = False
        elif i.isdigit() and c:
            print(i.isdigit())
            c = False
        elif i.islower() and d:
            print(i.islower())
            d = False
        elif i.isupper() and e:
            print(i.isupper())
            e = False
        elif (a, b, c, d == False):
            break
