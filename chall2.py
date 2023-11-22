def odd(n: int):
    if n % 2 != 0:
        return True
    return False


def even(n: int):
    if n % 2 == 0:
        return True
    return False


if __name__ == "__main__":
    n = int(input().strip())
    if odd(n):
        print("Weird")
    elif even(n) and n in range(2, 6):
        print("Not Weird")
    elif even(n) and n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
