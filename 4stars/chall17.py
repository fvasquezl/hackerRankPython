def mutate_string(string, position, character):
    string = string[:position] + character + string[position + 1 :]
    return string


if __name__ == "__main__":
    s = input()
    p, c = map(str, input().split())

    print(mutate_string(s, int(p), c))
