ls = [1, 2, 3, 2, 4]
element_to_remove = int(input("Enter the element to remove: "))
ls1 = []
found = False

for element in ls:
    if element == element_to_remove and not found:
        found = True
    else:
        ls1.append(element)

if not found:
    print(f"Element {element_to_remove} not found in the list.")
else:
    print(ls1) 
