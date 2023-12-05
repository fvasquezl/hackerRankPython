def split_and_join(line):
    # write your code here
    z = "-".join(list(map(str, line.split())))
    return z


if __name__ == "__main__":
    line = input()
    result = split_and_join(line)
    print(result)
