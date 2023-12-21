def average(array):
    # your code goes here
    a = set(array)

    p = sum(a) / len(a)

    return round(p, 3)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
