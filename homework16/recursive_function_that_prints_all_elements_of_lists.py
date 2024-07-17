def print_list_elements(ls):
    if not ls:
        return
    print(ls[0])
    print_list_elements(ls[1:])

lst = [1, 2, 3, 4, 5]
print_list_elements(lst)
