matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)

print("Original matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

for i in range(n):
    matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]

print("\nMatrix after swapping main and auxiliary diagonal elements:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
