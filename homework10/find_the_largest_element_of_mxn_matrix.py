matrix = [
    [1, 5, 3, 9],
    [4, 8, 2, 7],
    [6, 0, 11, 4]
]

N = len(matrix)
M = len(matrix[0])

largest_value = matrix[0][0]

for i in range(N):
    for j in range(M):
        if matrix[i][j] > largest_value:
            largest_value = matrix[i][j]

print(f"The largest value in the matrix is: {largest_value}")
