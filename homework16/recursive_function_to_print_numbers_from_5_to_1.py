def print_numbers(n):
    if n == 0:
        return
    else:
        print(n)
        print_numbers(n - 1)

print_numbers(5)
