def can_not_see(matrix):
    people_cant_see = []
    max_height = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] > max_height:
                max_height = matrix[i][j]
            else:
                temp = (i, j)
                people_cant_see.append(temp)
        max_height = 0
    return people_cant_see

matrix = [
    [1, 2, 3, 2, 1, 1],

    [2, 4, 4, 3, 7, 2],

    [5, 5, 2, 5, 6, 4],

    [6, 6, 7, 6, 7, 5]
]

print(can_not_see(matrix))