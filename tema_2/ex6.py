def search(matrix, x):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    aux = 0
    count = 0
    rez = []
    while aux != 10:
        for row in range(num_rows):
            for col in range(num_columns):
                if matrix[row][col] == aux:
                    count += 1
        if count == x:
            rez.append(aux)
        aux += 1
        count = 0
    return rez


matrix = [
    [1, 2, 3],
    [4, 1, 3],
    [7, 4, "test"]
]
print(search(matrix,2))