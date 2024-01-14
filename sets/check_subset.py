"""Main Module"""
if __name__ == "__main__":
    T = int(input())
    r = []
    for _ in range(T):
        a = int(input())
        a_set = set(map(int, input().split()))
        b = int(input())
        b_set = set(map(int, input().split()))

        if len(b_set.intersection(a_set).symmetric_difference(a_set)) == 0:
            r.append("True")
        else:
            r.append("False")

for x in r:
    print(x)
