i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)

print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)





def populate_numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

# Call the function with a limit of 6
populate_numbers(6)




def populate_numbers(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

# Call the function with a limit of 6 and an increment of 2
populate_numbers(6, 2)




def populate_numbers(limit, increment):
    numbers = []

    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)

    print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

# Call the function with a limit of 6 and an increment of 2
populate_numbers(6, 2)
