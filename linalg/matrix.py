matrix = [
    [1, 2, 1],
    [2, 6, 1],
    [1, 1, 4],
]

def scalar_mult(s, v):
    return [s * x for x in v]


def vector_add(v, w):
    assert len(v) == len(w)

    return [x + y for x, y in zip(v, w)]


def solve(m):
    # only regular case for now
    assert len(m) == len(m[0])

    for j in range(len(m)):
        assert m[j][j] != 0

        for i in range(j + 1, len(m)):
            l_ij = m[i][j] / m[j][j]
            m[i] = vector_add(m[i], scalar_mult(-l_ij, m[j]))


if __name__ == '__main__':
    solve(matrix)
    print(matrix)
