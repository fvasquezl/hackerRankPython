from itertools import permutations


def minion_game(string):
    # your code goes here
    vowels = "A", "E", "I", "O", "U"
    allwords = [
        "".join(j) for i in range(1, len(string) + 1) for j in permutations(string, i)
    ]

    startW = [w for w in allwords if w.startswith(vowels)]
    res = {}
    for i in startW:
        res[i] = startW.count(i)

    print(res)

    return


if __name__ == "__main__":
    s = input()
    minion_game(s)
