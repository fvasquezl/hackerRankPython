from itertools import permutations

if __name__ == "__main__":
    a, b = map(str, input().split())

    for i in list(permutations(sorted(a), int(b))):
        print("".join(i))
