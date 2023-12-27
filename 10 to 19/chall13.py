if __name__ == "__main__":
    arr = []
    first = float("inf")
    second = float(0)

    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        if score < first:
            second = first
            first = score
        else:
            if score > first and score <= second:
                second = score

    lista = [i for i in arr if i[1] == second]
    for i in sorted(lista):
        print(i[0])
