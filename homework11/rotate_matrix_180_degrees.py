matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = [list(row)[::-1] for row in matrix[::-1]]

for row in rotated_matrix:
    print(row)

