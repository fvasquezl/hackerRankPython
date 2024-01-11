# for i in range(
#     1, int(input()) + 1
# ):  # More than 2 lines will result in 0 score. Do not leave a blank line also
#     print([x for x in range(1, i)] + [x + 1 for x in range(0, i)][::-1])

for i in range(1, int(input()) + 1):
    print(map(int, [x for x in range(0, i)]))
