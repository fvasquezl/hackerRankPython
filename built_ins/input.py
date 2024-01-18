if __name__ == "__main__":
    x, n = list(map(int, input().split()))

    if eval(input().replace("x", f"{x}")) == n:
        print("True")
    else:
        print("False")

    # if (
    #     sum(
    #         list(
    #             eval(i.replace("x", f"{x}").strip())
    #             for i in map(str, input().split("+"))
    #         )
    #     )
    #     == n
    # ):
    #     print("True")
    # else:
    #     print("False")


"""
1 4
x**3 + x**2 + x + 1
"""
