def score_matrix(matrix):
    re = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            re += (-1)**(i+j) * matrix[i][j]
    return re
