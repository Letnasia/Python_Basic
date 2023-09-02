table = [
    [7],
    [5, 8],
    [9, 8, 2],
    [1, 3, 5, 6],
    [6, 2, 4, 4, 5],
    [9, 5, 3, 5, 5, 7],
    [7, 4, 6, 4, 7, 6, 8],
]


def dig(x, y):
    if x == len(table) - 1:
        return table[x][y]
    return table[x][y] + max(
        dig(x + 1, y),
        dig(x + 1, y + 1)
    )


print(dig(0, 0))

