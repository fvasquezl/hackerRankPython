from fractions import Fraction
import functools


def product(fracs):
    t = Fraction(functools.reduce(lambda x, y: x * y, fracs))
    # complete this line with a reduce statement
    return t.numerator, t.denominator


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
