arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_arr = []
odd_arr = []

for num in arr:
    if num % 2 == 0:
        even_arr.append(num)
    else:
        odd_arr.append(num)

arr = even_arr + odd_arr
print(arr)
