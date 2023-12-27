def merge_the_tools(string, k):
    # your code goes here

    for i in range(0, len(string), k):
        s = string[i : i + k]

        print("".join(list(dict.fromkeys(s))))

    return


if __name__ == "__main__":
    # string, k = input(), int(input())
    # merge_the_tools(string, k)
    merge_the_tools(
        "AABCAAADA",
        3,
    )
