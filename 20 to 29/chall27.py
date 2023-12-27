def print_rangoli(size):
    L = list(map(chr, range(97, size + 97)))
    lt = (len(L) * 2 - 1) * 2 - 1
    l1 = []
    fl = fr = ""
    for i in L[::-1]:
        l1.append(fl + i + fr)
        fr = i + fr
        fl = fl + i
    for i in l1[0:]:
        print("-".join(i).center(lt, "-"))
    for i in list(reversed(l1[:-1])):
        print("-".join(i).center(lt, "-"))
    return


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
