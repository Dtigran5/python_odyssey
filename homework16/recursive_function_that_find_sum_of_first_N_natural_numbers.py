def sum_of_natural_numbers(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_numbers(n-1)

n = 5
result = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is: {result}")
