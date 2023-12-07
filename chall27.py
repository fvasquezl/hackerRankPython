import textwrap


def print_rangoli(size):
    L = list(map(chr, range(97, size + 97)))
    lt = (len(L) * 2 - 1) * 2 - 1
    l1 = []
    l2 = []
    fl = fr = ""
    if lt > 1:
        for i in L[::-1]:
            l1.append(fl + i + fr)
            l2.insert(0, fl + i + fr)
            fr = i + fr
            fl = fl + i
        print((l1[0]).center(lt, "-"))
        for i in l1[1:]:
            print("-".join(i).center(lt, "-"))
        for i in l2[1:-1]:
            print("-".join(i).center(lt, "-"))
        print((l2[-1]).center(lt, "-"))
    else:
        print(L[0])
    return


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
