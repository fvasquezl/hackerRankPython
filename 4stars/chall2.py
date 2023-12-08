def odd(m: int):
    if m % 2 != 0:
        return True
    return False


if __name__ == "__main__":
    n = int(input().strip())
    if odd(n):
        print("Weird")
    elif n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
