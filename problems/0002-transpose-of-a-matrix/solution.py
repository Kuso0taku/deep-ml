def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    c = []
    for j in range(len(a[0])):
        b = []
        for i in range(len(a)):
            b.append(a[i][j])
        c.append(b)
    return c