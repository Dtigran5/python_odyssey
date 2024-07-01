n = int(input("Enter the number of elements in the array: "))
array = []

print("Enter the elements of the array:")
for i in range(n):
    element = int(input(f"Element {i+1}: "))
    array.append(element)

max_index = 0
min_index = 0

for i in range(1, n):
    if array[i] > array[max_index]:
        max_index = i
    if array[i] < array[min_index]:
        min_index = i

index_difference = abs(max_index - min_index)

print(f"The difference between the indices of the largest and smallest elements is: {index_difference}")
