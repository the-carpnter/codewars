def crossing_sum(matrix, row, col):
    m = matrix.copy()
    a = sum(m.pop(row))
    b = sum(i[col] for i in m)
    return a + b
