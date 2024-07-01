arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5]
arr_equal = True

if len(arr1) != len(arr2):
    arr_equal = False
else:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            arr_equal = False
            break

print(arr_equal) 