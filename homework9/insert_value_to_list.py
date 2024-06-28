ls = [1, 2, 4, 5]
value_to_insert = int(input("Enter value to insert: "))
index_to_insert = int(input("Enter index where to insert: "))
ls1 = []

for i in range(len(ls)):
    if i == index_to_insert:
        ls1.append(value_to_insert)
    ls1.append(ls[i])

if index_to_insert >= len(ls):
    ls.append(value_to_insert)
    print(ls)

print(ls1)
