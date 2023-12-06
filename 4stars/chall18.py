def swap_case(s):
    n = ""
    for i in s:
        n += i.lower() if i.isupper() else i.upper()
    return n


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
