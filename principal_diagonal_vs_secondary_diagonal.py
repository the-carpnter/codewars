def diagonal(matrix):
    p, s = [matrix[i][i] for i in range(len(matrix))], [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
    if sum(p) > sum(s):
        return 'Principal Diagonal win!'
    if sum(p) == sum(s):
        return 'Draw!'    
    return 'Secondary Diagonal win!'
