matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
diagonal_sum = 0

print("Matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

for i in range(n):
    diagonal_sum += matrix[i][i]

print(f"\nSum of main diagonal elements: {diagonal_sum}")
