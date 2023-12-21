cube = lambda x: x**3  # complete the lambda function


def fibonacci(n):
    a, b = 0, 1
    l1 = []
    for i in range(n):
        l1.append(a)
        a, b = b, a + b
    return l1


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
