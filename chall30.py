def merge_the_tools(string, k):
    # your code goes here
    # substrings = len(string) / k
    for i in range(0, len(string), k):
        s = string[i : i + k]
        for j, c in enumerate(s):
            if c in s[j + 1 :]:
                s = s[:j] + s[j + 1 :]

        print(s)
    return


if __name__ == "__main__":
    # string, k = input(), int(input())
    # merge_the_tools(string, k)
    merge_the_tools("AABCAAADA", 3)
