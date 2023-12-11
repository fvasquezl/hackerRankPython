from timeit import default_timer as timer


def minion_game(string):
    # your code goes here
    vowels = "A", "E", "I", "O", "U"
    # mlist = list(string)
    s = 0
    k = 0
    # start = timer()
    # for i, c in enumerate(string):
    #     if c in vowels:
    #         k += len(string[i:])
    #     else:
    #         s += len(string[i:])
    # end = timer()
    # print(end - start)

    # start = timer()
    # s = len(mlist)
    # for i in range(len(mlist)):
    #     if string[i] in vowels:
    #         k += s - i
    #     else:
    #         s += s - i
    # end = timer()
    # print(end - start)

    # start = timer()
    # for i in range(len(mlist)):
    #     if mlist[i] in vowels:
    #         k += len(mlist[i:])
    #     else:
    #         s += len(mlist[i:])
    # end = timer()
    # print(end - start)
    ls = len(string)
    start = timer()
    for i, c in enumerate(string):
        if c in vowels:
            k += ls - i
        else:
            s += ls - i
    end = timer()
    print(end - start)

    if k > s:
        print(f"Kevin {k}")
    elif s > k:
        print(f"Stuart {s}")
    else:
        print("Draw")
    return


if __name__ == "__main__":
    # s = input()
    minion_game("BANANA")
