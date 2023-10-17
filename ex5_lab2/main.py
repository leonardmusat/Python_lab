def zero(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    for row in range(num_rows):
        for col in range(num_columns):
            if row > col:
                matrix[row][col] = 0

    return matrix


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(zero(matrix))