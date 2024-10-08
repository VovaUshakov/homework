def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        lines = []
        matrix.append(lines)
        for k in range(m):
            lines.append(value)
    print(matrix)
    matrix = []
    return matrix


matrix = get_matrix(3, 2, 1)
