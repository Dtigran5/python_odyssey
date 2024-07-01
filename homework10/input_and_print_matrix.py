n = int(input("Enter the size of the square matrix: "))
matrix = []

print("Enter the elements of the matrix row by row:")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Element [{i},{j}]: "))
        row.append(element)
    matrix.append(row)

print("The elements of the matrix are:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
