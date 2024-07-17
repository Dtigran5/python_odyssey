def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)

num = 5
print(f"the factorial of {num} is {recursive_factorial(num)}")