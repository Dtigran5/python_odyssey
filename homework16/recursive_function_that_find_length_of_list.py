def find_length(ls):
    if not ls:
        return 0
    else:
        return 1 + find_length(ls[1:])

ls1 = [1, 2, 3, 4, 5]
print(f"the length of list is {find_length(ls1)}")  
