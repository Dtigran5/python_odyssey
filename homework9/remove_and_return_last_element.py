ls = [1, 2, 3]

if len(ls) == 0:
    print("The list is empty.")
else:
    last_element = ls[-1]
    ls1 = ls[:-1]
    print(f"Removed element: {last_element}")
    print(f"New list: {ls1}")
