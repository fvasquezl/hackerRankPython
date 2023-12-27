def print_formatted(number):
    # your code goes here
    print(len(str(format(number, "b"))))
    for i in range(1, number + 1):
        print(
            str(int(i)).rjust(len(str(format(number, "b"))), " "),
            str(format(i, "o")).rjust(len(str(format(number, "b"))), " "),
            str(format(i, "X")).rjust(len(str(format(number, "b"))), " "),
            str(format(i, "b")).rjust(len(str(format(number, "b"))), " "),
        )
    return


if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
