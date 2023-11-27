import heapq

if __name__ == "__main__":
    arr = [
        ("Rachel", -50),
        ("Mawer", -50),
        ("Sheen", -50),
        ("Shaheen", 51),
    ]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     arr.append((name, score))
    lowest_elements = set(arr)
    print(lowest_elements)
    second_score = sorted(lowest_elements)[1][-1]

    el = sorted([list(i) for i in arr if i[1] == second_score])

    for i in el:
        print(i[0])
