def difference(a, a1):
    # your code goes here
    for i in a.symmetric_difference(a1):
        print(i)
    return


if __name__ == "__main__":
    n = int(input())
    a = set(map(int, input().split()))
    n1 = int(input())
    a1 = set(map(int, input().split()))
    result = difference(a, a1)
