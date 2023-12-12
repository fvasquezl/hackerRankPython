"""
1 2
3 4
"""


from itertools import product


def cartesian_product(l1, l2):
    x = [l1, l2]
    p = list(product(*x))
    return " ".join(str(e) for e in p)


if __name__ == "__main__":
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    print(cartesian_product(l1, l2))
