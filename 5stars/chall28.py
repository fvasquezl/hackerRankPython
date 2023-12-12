#!/bin/python3


# Complete the solve function below.
def solve(s):
    l = s.split(" ")

    for i in range(len(l)):
        if l[i] != "":
            if l[i][0].isalpha():
                l[i] = l[i][0].upper() + l[i][1:]
    return " ".join(l)


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()
