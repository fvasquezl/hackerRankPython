if __name__ == "__main__":
    for i in range(
        1, int(input())
    ):  # More than 2 lines will result in 0 score. Do not leave a blank line also
        # p = list(map(a + 1, range(i, 1)))

        print(sum(list(map(lambda num: i * 10 ** (i - num), range(1, i + 1)))))
