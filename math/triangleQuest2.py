for i in range(
    1, int(input()) + 1
):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    # print(
    #     sum(
    #         list(
    #             x * (10**j)
    #             for j, x in enumerate(
    #                 [x + 1 for x in range(0, i)] + [x for x in range(1, i)][::-1]
    #             )
    #         )
    #     )
    # )

    # print(
    #     sum(
    #         list(
    #             (x + 1) * (10**j)
    #             for j, x in enumerate([*range(0, i)] + [*range(0, i)][::-1][1:])
    #         )
    #     )
    # )

    print(
        sum(
            list(
                x * (10**j) for j, x in enumerate([*range(1, i)] + [*range(i, 0, -1)])
            )
        )
    )

    # print(
    #     sum(
    #         list(
    #             map(
    #                 lambda x: x[1] * (10 ** x[0]),
    #                 enumerate([*range(1, i)] + [*range(i, 0, -1)]),
    #             )
    #         )
    #     )
    # )
