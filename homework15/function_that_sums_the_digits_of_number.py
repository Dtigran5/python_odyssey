def sum_of_digits(number):
    number_str = str(number)
    total = 0
    for digit in number_str:
        total += int(digit)
    return total

number = 123
print(sum_of_digits(number))  
